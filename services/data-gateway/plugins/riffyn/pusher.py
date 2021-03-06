from collections import defaultdict

import riffyn_nexus_sdk_v1 as api
import requests

from lib import riffyn, utils
from plugins import registry
from plugins.riffyn.config import PluginConfig

cfg = PluginConfig()


class UnprocessableSource(BaseException):
    pass


class Pusher(registry.Pusher):
    def __init__(self, logger):
        super(registry.Pusher, self).__init__()

        self.logger = logger
        self.control_tower_url = cfg.CONTROL_TOWER_URL

        client = riffyn.Client.default(cfg.API_KEY)
        self.activity_api = api.ProcessActivityApi(client)
        self.experiment_api = api.ExperimentApi(client)
        self.run_api = api.RunApi(client)

    def push(self, uuid, rows):
        try:
            # Fetch the protocol trigger for the UUID
            trigger = self.__get_trigger(uuid)
            # Parse the trigger's metadata on Riffyn
            metadata = self.__parse_metadata(trigger)
            # Merge the data rows for each well
            indexes = self.__build_indexes(rows)

            self.logger.info(
                "data.push.started", uuid=uuid, indexes=len(indexes), rows=len(rows)
            )

            # If the protocol is plate-based
            if isinstance(metadata, list):
                for index, data in indexes.items():
                    # Error if the well index exceeds the metadata size
                    if index > len(metadata) - 1:
                        raise ValueError(f"index {index} exceeds metadata size")

                    experiment_id, activity_id, run_id = metadata[index]
                    activity = self.activity_api.get_activity(
                        experiment_id, activity_id
                    )

                    # Populate the run with the data for the well
                    self.__populate(experiment_id, run_id, activity, data)

            else:
                experiment_id, activity_id, run_id = metadata
                activity = self.activity_api.get_activity(experiment_id, activity_id)
                data = next(iter(indexes.values()))

                # Populate the run with the data
                self.__populate(experiment_id, run_id, activity, data)

            self.logger.info(
                "data.push.finished", uuid=uuid, indexes=len(indexes), rows=len(rows)
            )

        except UnprocessableSource:
            self.logger.error("data.push.skipped", uuid=uuid)
            return  # No-op

        except api.rest.ApiException as err:
            self.logger.error(
                "data.push.failed",
                uuid=uuid,
                status=err.status,
                error=err.reason,
            )

        except Exception as err:
            self.logger.error("data.push.failed", uuid=uuid, error=err)

    def __get_trigger(self, uuid):
        resp = requests.get(f"{self.control_tower_url}/triggers/{uuid}")
        resp.raise_for_status()
        return resp.json()

    def __parse_metadata(self, trigger):
        # Only handle triggers from Riffyn
        metadata = trigger["metadata"]
        if metadata["source"] != "riffyn":
            raise UnprocessableSource

        # Extract the experiment, activity and run ID for each well index
        spec = metadata["spec"]
        if isinstance(spec, list):
            return list(
                map(
                    lambda index: (
                        index["experimentId"],
                        index["activityId"],
                        index["runId"],
                    ),
                    spec,
                )
            )

        else:
            return (spec["experimentId"], spec["activityId"], spec["runId"])

    def __build_indexes(self, rows):
        # Combine {"index": 1, "data": {"a": 1, "b": 2}}, {"index": 1, "data": {"a": 2, "b": 3}}
        # into {"1": {"a": [1, 2], "b": [2, 3]}} for each well index
        indexes = {}
        for row in rows:
            if row.index not in indexes:
                indexes[row.index] = defaultdict(list)

            for key, value in row.data.items():
                indexes[row.index][key].append(str(value))

        return indexes

    def __populate(self, experiment_id, run_id, activity, data):
        # Create multi-valued data using primary keys in Riffyn
        pkeys = self.__build_pkeys(run_id, activity, data)
        rows = self.run_api.add_batch_run_data(
            api.AddBatchDataToInputBody(pkeys), experiment_id, activity.id
        )

        # Use the multi-valued data row IDs to push the remaining dataset
        dataset = self.__build_dataset(run_id, activity, rows[0], data)
        rows = self.run_api.add_batch_run_data(
            api.AddBatchDataToInputBody(dataset), experiment_id, activity.id
        )

    def __build_pkeys(self, run_id, activity, data):
        # NOTE: Assume the last output in the activity is the one to be populated
        output = activity.outputs[-1]
        pkey = next(iter(data.keys()))

        # NOTE: Keys in data have to camel-cased
        if pkey != utils.str_to_camelcase(output.properties[0].name):
            raise ValueError(
                f"primary key does not match: expected '{output.properties[0].name}', got '{pkey}'"
            )

        return [
            {
                "resourceDefId": output.id,
                "propertyTypeId": output.properties[0].id,
                "runIds": [run_id],
                "values": data[pkey],
                "append": True,
            }
        ]

    def __build_dataset(self, run_id, activity, rows, data):
        # NOTE: Assume the last output in the activity is the one to be populated
        output = activity.outputs[-1]
        dataset = []

        # Build payload for batch data request to Riffyn
        for property in output.properties[1:]:
            pname = utils.str_to_camelcase(property.name)
            # Verify that the output property is available in the dataset
            self.__verify_data(pname, rows, data)

            values = []
            for i, row in enumerate(rows["data"]):
                value = data[pname][i]
                if value:
                    values.append(
                        {
                            "eventId": str(row["eventId"]),
                            "value": value,
                        }
                    )

            if values:
                dataset.append(
                    {
                        "resourceDefId": output.id,
                        "propertyTypeId": property.id,
                        "eventGroupId": rows["eventGroupId"],
                        "runIds": [run_id],
                        "values": values,
                    }
                )

        return dataset

    def __verify_data(self, property, rows, data):
        if property not in data:
            raise ValueError(f"could not find property in data: {property}")

        expected = len(rows["data"])
        actual = len(data[property])

        if actual != expected:
            raise ValueError(
                f"unexpected number of values for '{property}': expected {expected}, found {actual}"
            )
