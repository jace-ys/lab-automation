import re
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

        self.partials = {}

    def run(self):
        while not self.done.is_set():
            self.logger.info("runs.poll.started")

            try:
                runs = self.__fetch_run_statuses()
                for experiment_id, runs in runs.items():
                    for run in runs["started"]:
                        complete, plate = self.__aggregate(run)
                        if len(complete) > 0:
                            if plate:
                                commands = self.__build_commands(
                                    experiment_id, complete, plate
                                )
                            else:
                                commands = self.__build_commands(
                                    experiment_id, complete
                                )

                            for cmd in commands:
                                self.queue.put(cmd)

                        self.cache.hset(self.cache_key, run.id, "")
                        self.logger.info(
                            "run.started",
                            experiment_id=experiment_id,
                            run_id=run.id,
                            run_name=run.name,
                        )

                    for run in runs["stopped"]:
                        partial = self.__is_partial(run)
                        if partial:
                            key, rows, cols, idx = partial
                            if key in self.partials:
                                self.partials[key][idx] = None

                        self.logger.info(
                            "run.stopped",
                            experiment_id=experiment_id,
                            run_id=run.id,
                            run_name=run.name,
                        )
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

                elif (
                    run.status == "stopped" or run.status == "new"
                ) and run.id in active_runs:
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

    def __aggregate(self, run):
        partial = self.__is_partial(run)
        if not partial:
            return [run], None

        key, rows, cols, idx = partial
        if key not in self.partials:
            # Pre-fill an array equal to the number of expected partials
            self.partials[key] = [None] * (rows * cols)
        self.partials[key][idx] = run

        # Check that all partial runs in the aggregated set have been populated
        if all(partial is not None for partial in self.partials[key]):
            return self.partials[key], (rows, cols)

        return [], None

    def __is_partial(self, run):
        partial = re.search(r"(.*) \[([1-9])+x([1-9])+\] ([1-9])+$", run.name)
        if not partial:
            return False

        name, rows, cols, idx = partial.group(1, 2, 3, 4)
        key = f"{self.cache_key}/{run.activity_id}/{name}"
        return (key, int(rows), int(cols), int(idx) - 1)

    def __build_commands(self, experiment_id, runs, plate=None):
        # Create a mapping of resource IDs -> names
        resources = {}
        # Create a mapping of API version -> command objects
        commands = {}

        for idx, run in enumerate(runs):
            activity = self.activity_api.get_activity(experiment_id, run.activity_id)

            # All runs in an aggregated shape should have the same shape so use the first
            # in each set as the command template
            if idx == 0:
                # Iterate over each input in the run and populate the mappings
                for input in run.inputs:
                    try:
                        api_version = input.resource_name
                        protocol = activity.name.replace(" ", "")

                        cmd = command.Command(api_version, protocol)
                        if len(runs) > 1:
                            cmd.plate(*plate)
                            # Pre-fill the spec with an array equal to the number of runs
                            cmd.spec = [{}] * len(runs)
                            cmd.metadata(
                                "riffyn",
                                list(
                                    map(
                                        lambda run: {
                                            "experimentId": experiment_id,
                                            "activityId": run.activity_id,
                                            "runId": run.id,
                                        },
                                        runs,
                                    )
                                ),
                            )
                            commands[api_version] = cmd
                        else:
                            cmd.metadata(
                                "riffyn",
                                {
                                    "experimentId": experiment_id,
                                    "activityId": run.activity_id,
                                    "runId": run.id,
                                },
                            )

                        # Track created command and its associated API version
                        commands[api_version] = cmd
                        resources[input.resource_def_id] = api_version

                    except command.InvalidAPIVersion:
                        continue

            data = self.__get_experiment_data_raw(experiment_id, activity.id, run)
            datatable = data["datatables"][run.id]["datatable"][0]

            # Iterate over each input in the activity and populate the commands' spec
            for input in activity.inputs:
                properties = {}
                if input.id in resources:
                    # Get the API version for the resource
                    api_version = resources[input.id]

                    for property in input.properties:
                        header = f"{activity.id} | input | {input.id} | {property.id} | value"
                        if datatable[header] is not None:
                            properties[
                                utils.str_to_camelcase(property.name)
                            ] = datatable[header]

                if isinstance(commands[api_version].spec, list):
                    commands[api_version].spec[idx] = {
                        **commands[api_version].spec[idx],
                        **properties,
                    }
                else:
                    commands[api_version].spec.update(properties)

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
