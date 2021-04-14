from collections import defaultdict

import riffyn_nexus_sdk_v1 as api
import requests

from lib import riffyn, utils
from plugins import pushers
from plugins.riffyn.config import PluginConfig

cfg = PluginConfig()


class UnprocessableSource(BaseException):
    pass


class Pusher(pushers.Pusher):
    def __init__(self, logger):
        super(pushers.Pusher, self).__init__()

        self.logger = logger
        self.control_tower_addr = cfg.CONTROL_TOWER_ADDR

        client = riffyn.Client.default(cfg.API_KEY)
        self.activity_api = api.ProcessActivityApi(client)
        self.experiment_api = api.ExperimentApi(client)
        self.run_api = api.RunApi(client)

    def push(self, uuid, rows):
        try:
            command = self.__get_command(uuid)
            metadata = self.__parse_metadata(command)
            indexes = self.__build_indexes(rows)

            self.logger.info(
                "data.push.started", uuid=uuid, indexes=len(indexes), rows=len(rows)
            )

            if isinstance(metadata, list):
                for index, data in indexes.items():
                    if index > len(metadata) - 1:
                        raise ValueError(f"index {index} exceeds metadata size")

                    experiment_id, activity_id, run_id = metadata[index]
                    activity = self.activity_api.get_activity(
                        experiment_id, activity_id
                    )

                    self.__populate(experiment_id, run_id, activity, data)

            else:
                experiment_id, activity_id, run_id = metadata
                activity = self.activity_api.get_activity(experiment_id, activity_id)
                data = next(iter(indexes.values()))

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

    def __get_command(self, uuid):
        resp = requests.get(f"http://{self.control_tower_addr}/commands/{uuid}")
        resp.raise_for_status()
        return resp.json()

    def __parse_metadata(self, command):
        source = command["metadata"]["source"]
        if source["name"] != "riffyn":
            raise UnprocessableSource

        spec = source["spec"]
        if isinstance(spec, list):
            metadata = []
            for index in spec:
                metadata.append(
                    (index["experimentId"], index["activityId"], index["runId"])
                )
        else:
            metadata = (spec["experimentId"], spec["activityId"], spec["runId"])

        return metadata

    def __build_indexes(self, rows):
        indexes = {}
        for row in rows:
            if row.index not in indexes:
                indexes[row.index] = defaultdict(list)

            for key, value in row.data.items():
                indexes[row.index][key].append(str(value))

        return indexes

    def __populate(self, experiment_id, run_id, activity, data):
        pkeys = self.__build_pkeys(run_id, activity, data)
        rows = self.run_api.add_batch_run_data(
            api.AddBatchDataToInputBody(pkeys), experiment_id, activity.id
        )

        # NOTE: Assume the activity only has a single output resource to be populated
        dataset = self.__build_dataset(run_id, activity, rows[0], data)
        rows = self.run_api.add_batch_run_data(
            api.AddBatchDataToInputBody(dataset), experiment_id, activity.id
        )

    def __build_pkeys(self, run_id, activity, data):
        # NOTE: Assume the activity only has a single output resource to be populated
        output = activity.outputs[0]
        pkey = next(iter(data.keys()))

        # NOTE: Assume keys in data are camel-cased
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
        # NOTE: Assume the activity only has a single output resource to be populated
        output = activity.outputs[0]
        dataset = []

        for property in output.properties[1:]:
            pname = utils.str_to_camelcase(property.name)
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
        # NOTE: Assume keys in data are camel-cased
        if property not in data:
            raise ValueError(f"could not find property in data: {property}")

        expected = len(rows["data"])
        actual = len(data[property])

        if actual != expected:
            raise ValueError(
                f"unexpected number of values for '{property}': expected {expected}, found {actual}"
            )
