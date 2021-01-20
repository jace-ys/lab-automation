from collections import defaultdict

import swagger_client as riffyn

from lib import utils
from plugins.riffyn.config import PluginConfig

EXPERIMENT_ID = "i3hoxbubYkvpGQaYc"
ACTIVITY_ID = "jZYi3XYkQixxGM4x4"
RUN_ID = "Bf5rTf7mw3xLxaMYw"

cfg = PluginConfig()


class Pusher:
    def __init__(self, logger):
        super(Pusher, self).__init__()

        self.logger = logger

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def push(self, payload):
        try:
            kv_data, rows = self.__merge_data(payload.data)
            self.logger.info("data.push.started", uuid=payload.uuid, rows=rows)

            # TODO: Find experiment, activity and run IDs from payload.uuid
            activity = self.activity_api.get_activity(EXPERIMENT_ID, ACTIVITY_ID)

            output_pkeys = self.__populate_output_pkeys(activity, RUN_ID, kv_data)
            output_rows = self.__add_batch_run_data(
                EXPERIMENT_ID, ACTIVITY_ID, output_pkeys
            )

            output_data = self.__populate_output_data(
                activity, RUN_ID, kv_data, output_rows
            )
            output_rows = self.__add_batch_run_data(
                EXPERIMENT_ID, ACTIVITY_ID, output_data
            )

            self.logger.info("data.push.finished", uuid=payload.uuid, rows=rows)

        except riffyn.rest.ApiException as err:
            self.logger.error("data.push.failed", status=err.status, error=err.reason)
            raise

        except Exception as err:
            self.logger.error("data.push.failed", error=err)
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

    def __populate_output_pkeys(self, activity, run_id, kv_data):
        # NOTE: Assume the activity only has a single output to be populated
        output = activity.outputs[0]
        output_pkeys = []

        pkey = next(iter(kv_data.keys()))
        if pkey.lower() != utils.str_to_snakecase(output.properties[0].name).lower():
            raise ValueError(
                f'primary key does not match: expected "{output.properties[0].name}", got "{pkey}"'
            )

        output_pkeys.append(
            {
                "resourceDefId": output.id,
                "propertyTypeId": output.properties[0].id,
                "runIds": [run_id],
                "values": kv_data[pkey],
                "append": True,
            }
        )

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
