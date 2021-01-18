import swagger_client as riffyn

from lib import utils
from plugins.riffyn.config import PluginConfig

EXPERIMENT_ID = "gRcE4bogh6T94cNJs"
ACTIVITY_ID = "e6MDoEZjgw7GCytJx"
RUN_ID = "uykxenRDCuvhxKLS8"

cfg = PluginConfig()


class Pusher:
    def __init__(self, logger):
        super(Pusher, self).__init__()

        self.logger = logger
        self.cache_key = cfg.CACHE_KEY

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def push(self, payload):
        # TODO: find experiment, activity and run IDs from payload.uuid
        activity = self.activity_api.get_activity(EXPERIMENT_ID, ACTIVITY_ID)
        data_rows = self.__make_rows(payload.data)

        output_pkeys = self.__populate_output_pkeys(activity, RUN_ID, data_rows)
        output_rows = self.__add_batch_run_data(
            EXPERIMENT_ID, ACTIVITY_ID, output_pkeys
        )

        output_data = self.__populate_output_data(
            activity, RUN_ID, data_rows, output_rows
        )
        output_rows = self.__add_batch_run_data(EXPERIMENT_ID, ACTIVITY_ID, output_data)

    def __make_rows(self, dataset):
        if isinstance(dataset, list):
            return dataset
        else:
            return [dataset]

    def __populate_output_pkeys(self, activity, run_id, data_rows):
        # Assume the activity only has a single output to be populated
        output = activity.outputs[0]
        output_pkeys = []

        values = list(map(lambda row: next(iter(row.values())), data_rows))
        output_pkeys.append(
            {
                "resourceDefId": output.id,
                "propertyTypeId": output.properties[0].id,
                "runIds": [run_id],
                "values": values,
                "append": True,
            }
        )

        return output_pkeys

    def __populate_output_data(self, activity, run_id, data_rows, output_rows):
        # Assume the activity only has a single output to be populated
        output = activity.outputs[0]
        output_data = []

        for j, property in enumerate(output.properties[1:]):
            values = list(map(lambda row: list(row.values())[j + 1], data_rows))
            output_data.append(
                {
                    "resourceDefId": output.id,
                    "propertyTypeId": property.id,
                    "eventGroupId": output_rows[0]["eventGroupId"],
                    "runIds": [run_id],
                    "values": [
                        {
                            "eventId": str(row["eventId"]),
                            "value": values[k],
                        }
                        for k, row in enumerate(output_rows[0]["data"])
                    ],
                }
            )

        return output_data

    def __add_batch_run_data(self, experiment_id, activity_id, data):
        return self.run_api.add_batch_run_data(
            riffyn.AddBatchDataToInputBody(data), experiment_id, activity_id
        )
