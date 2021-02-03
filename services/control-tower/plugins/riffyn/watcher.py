import threading

import requests
import swagger_client as riffyn

from lib import utils
from plugins.riffyn.config import PluginConfig
from src.commands import command

cfg = PluginConfig()


class Watcher(threading.Thread):
    def __init__(self, logger, cache, queue, done):
        super(Watcher, self).__init__()

        self.logger = logger
        self.cache = cache
        self.queue = queue
        self.done = done
        self.cache_key = cfg.CACHE_KEY
        self.poll_interval = cfg.POLL_INTERVAL

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def run(self):
        while not self.done.is_set():
            self.logger.info("runs.poll.started")

            try:
                runs = self.__fetch_run_statuses()
                for experiment_id, runs in runs.items():
                    for run in runs["started"]:
                        for cmd in self.__build_commands(experiment_id, run):
                            self.queue.put(cmd)

                        self.cache.hset(self.cache_key, run.id, "")
                        self.logger.info("run.started", run_id=run.id)

                    for run in runs["stopped"]:
                        self.logger.info("run.stopped", run_id=run.id)
                        self.cache.hdel(self.cache_key, run.id)

                self.logger.info("runs.poll.finished")

            except riffyn.rest.ApiException as err:
                self.logger.error(
                    "runs.poll.failed", status=err.status, error=err.reason
                )

            except Exception as err:
                self.logger.error("runs.poll.failed", error=err)

            self.done.wait(self.poll_interval)

    def __fetch_run_statuses(self):
        experiments = self.__fetch_experiments()
        active_runs = self.cache.hgetall(self.cache_key)

        runs = {}
        for experiment in experiments:
            status = {"started": [], "stopped": []}
            for run in self.__fetch_runs(experiment.id):
                if run.status == "running" and run.id not in active_runs:
                    status["started"].append(run)

                elif run.status == "stopped" and run.id in active_runs:
                    status["stopped"].append(run)

            runs[experiment.id] = status

        return runs

    def __fetch_experiments(self):
        experiments = self.experiment_api.list_experiments()
        return experiments.data

    def __fetch_runs(self, experiment_id):
        groups = self.run_api.list_run_groups(experiment_id)
        runs = list(
            map(
                lambda group: self.run_api.list_runs(experiment_id, group.id).data,
                groups.data,
            )
        )
        return utils.flatten(runs)

    def __build_commands(self, experiment_id, run):
        activity = self.activity_api.get_activity(experiment_id, run.activity_id)
        data = self.__get_experiment_data_raw(experiment_id, activity.id, run)
        datatable = data["datatables"][run.id]["datatable"][0]

        # Create a mapping of resource IDs -> names
        resources = {}
        # Create a mapping of API version -> command objects
        commands = {}

        # Iterate over each input in the run and populate the mappings
        for input in run.inputs:
            try:
                api_version = input.resource_name
                protocol = activity.name.replace(" ", "")

                cmd = command.Command(api_version, protocol)
                cmd.metadata(
                    "riffyn",
                    {
                        "experimentId": experiment_id,
                        "activityId": run.activity_id,
                        "runId": run.id,
                    },
                )

                resources[input.resource_def_id] = api_version
                commands[api_version] = cmd

            except command.InvalidAPIVersion:
                continue

        # Iterate over each input in the activity and populate the commands' spec
        for input in activity.inputs:
            if input.id not in resources:
                continue

            # Get the name (API version) for this resource
            api_version = resources[input.id]
            properties = {}

            for property in input.properties:
                header = f"{activity.id} | input | {input.id} | {property.id} | value"
                properties[utils.str_to_camelcase(property.name)] = datatable[header]

            commands[api_version].spec[utils.str_to_camelcase(input.name)] = properties

        return list(commands.values())

    def __get_experiment_data_raw(self, experiment_id, activity_id, run):
        resp = requests.get(
            f"https://api.app.riffyn.com/v1/experiment/{experiment_id}/step/{activity_id}/data/raw",
            headers={"api-key": cfg.API_KEY},
            params={
                "rgid": [run.group_id],
                "rid": [run.id],
                "rnum": [run.num],
            },
        )
        resp.raise_for_status()
        return resp.json()
