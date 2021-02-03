from collections import defaultdict

import requests
import swagger_client as riffyn

from lib import utils
from plugins.riffyn.config import PluginConfig

cfg = PluginConfig()


class UnprocessableSource(BaseException):
    pass


class Pusher:
    def __init__(self, logger):
        super(Pusher, self).__init__()

        self.logger = logger
        self.control_tower_addr = cfg.CONTROL_TOWER_ADDR

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def push(self, payload):
        try:
            kv_data, rows = self.__merge_data(payload.data)
            self.logger.info("data.push.started", uuid=payload.uuid, rows=rows)

            cmd = self.__get_command_metadata(payload.uuid)
            experiment_id, activity_id, run_id = self.__parse_riffyn_metadata(cmd)
            activity = self.activity_api.get_activity(experiment_id, activity_id)

            output_pkeys = self.__populate_output_pkeys(activity, run_id, kv_data)
            output_rows = self.__add_batch_run_data(
                experiment_id, activity_id, output_pkeys
            )

            output_data = self.__populate_output_data(
                activity, run_id, kv_data, output_rows
            )
            output_rows = self.__add_batch_run_data(
                experiment_id, activity_id, output_data
            )

            self.logger.info("data.push.finished", uuid=payload.uuid, rows=rows)

        except UnprocessableSource:
            self.logger.error("data.push.skipped", uuid=payload.uuid)
            return  # No-op

        except riffyn.rest.ApiException as err:
            self.logger.error(
                "data.push.failed",
                uuid=payload.uuid,
                status=err.status,
                error=err.reason,
            )
            raise

        except Exception as err:
            self.logger.error("data.push.failed", uuid=payload.uuid, error=err)
            raise

    def __merge_data(self, data):
        if isinstance(data, list):
            rows = data
        else:
            rows = [data]

        properties = defaultdict(list)
        for row in rows:
            for key, value in row.items():
                properties[key.lower()].append(value)

        return dict(properties), len(rows)

    def __get_command_metadata(self, uuid):
        resp = requests.get(f"http://{self.control_tower_addr}/commands/{uuid}")
        resp.raise_for_status()
        return resp.json()

    def __parse_riffyn_metadata(self, command):
        source = command["metadata"]["source"]
        if source["name"] != "riffyn":
            raise UnprocessableSource

        spec = source["spec"]
        experiment_id = spec["experimentId"]
        activity_id = spec["activityId"]
        run_id = spec["runId"]

        return experiment_id, activity_id, run_id

    def __populate_output_pkeys(self, activity, run_id, kv_data):
        # NOTE: Assume the activity only has a single output to be populated
        output = activity.outputs[0]

        pkey = next(iter(kv_data.keys()))
        # NOTE: Assume keys in data are snake-cased
        if pkey.lower() != utils.str_to_snakecase(output.properties[0].name).lower():
            raise ValueError(
                f'primary key does not match: expected "{output.properties[0].name}", got "{pkey}"'
            )

        output_pkeys = [
            {
                "resourceDefId": output.id,
                "propertyTypeId": output.properties[0].id,
                "runIds": [run_id],
                "values": kv_data[pkey],
                "append": True,
            }
        ]
        return output_pkeys

    def __populate_output_data(self, activity, run_id, kv_data, output_rows):
        # NOTE: Assume the activity only has a single output to be populated
        output = activity.outputs[0]
        output_data = []

        for property in output.properties[1:]:
            property_name = utils.str_to_snakecase(property.name).lower()

            if property_name not in kv_data:
                raise ValueError(f"could not find property with key: {property.name}")

            if len(kv_data[property_name]) != len(output_rows["data"]):
                raise ValueError(
                    f'unexpected number of values for "{property.name}": expected {len(output_rows["data"])}, found {len(kv_data[property_name])}'
                )

            output_data.append(
                {
                    "resourceDefId": output.id,
                    "propertyTypeId": property.id,
                    "eventGroupId": output_rows["eventGroupId"],
                    "runIds": [run_id],
                    "values": [
                        {
                            "eventId": str(row["eventId"]),
                            "value": kv_data[property_name][idx],
                        }
                        for idx, row in enumerate(output_rows["data"])
                    ],
                }
            )

        return output_data

    def __add_batch_run_data(self, experiment_id, activity_id, data):
        output_rows = self.run_api.add_batch_run_data(
            riffyn.AddBatchDataToInputBody(data), experiment_id, activity_id
        )
        # NOTE: Assume the activity only has a single output to be populated
        return output_rows[0]
