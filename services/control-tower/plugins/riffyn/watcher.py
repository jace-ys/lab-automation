import random
import threading

import swagger_client as riffyn

from lib import utils
from plugins.riffyn.config import PluginConfig
from src.commands import command

cfg = PluginConfig()


class Watcher(threading.Thread):
    def __init__(self, logger, redis, queue, done):
        super(Watcher, self).__init__()

        self.logger = logger
        self.redis = redis
        self.queue = queue
        self.done = done
        self.cache_key = cfg.CACHE_KEY
        self.poll_interval = cfg.POLL_INTERVAL

        riffyn.Configuration().api_key["api-key"] = cfg.API_KEY
        self.activity_api = riffyn.ProcessActivityApi()
        self.experiment_api = riffyn.ExperimentApi()
        self.run_api = riffyn.RunApi()

    def __fetch_runs(self, experiment_id):
        groups = self.run_api.list_run_groups(experiment_id)
        runs = list(
            map(
                lambda group: self.run_api.list_runs(experiment_id, group.id).data,
                groups.data,
            )
        )

        return utils.flatten(runs)

    def __fetch_experiments(self):
        experiments = self.experiment_api.list_experiments()

        return experiments.data

    def __build_command(self, process_id, run):
        activity = self.activity_api.get_activity(process_id, run.activity_id)

        # NOTE: Assume the first resource is the target
        api_version = run.inputs[0].resource_name
        protocol = activity.name.replace(" ", "")

        cmd = command.Command(api_version, protocol)

        for input in activity.inputs:
            properties = {}
            for property in input.properties:
                # TODO: Get property values
                properties[utils.to_camelcase(property.name)] = random.randint(0, 100)

            cmd.spec[utils.to_camelcase(input.name)] = properties

        return cmd

    def __fetch_run_statuses(self):
        experiments = self.__fetch_experiments()
        active_runs = self.redis.hgetall(self.cache_key)

        runs = {}
        for experiment in experiments:
            status = {"started": [], "stopped": []}

            for run in self.__fetch_runs(experiment.id):
                if run.status == "running" and run.id not in active_runs:
                    status["started"].append(run)

                elif run.status == "stopped" and run.id in active_runs:
                    status["stopped"].append(run)

            # Associate started runs with each experiment's process ID
            runs[experiment.top_group.id] = status

        return runs

    def run(self):
        while not self.done.is_set():
            try:
                self.logger.info("runs.poll.started")
                runs = self.__fetch_run_statuses()

                for process_id, runs in runs.items():
                    for run in runs["started"]:
                        self.logger.info("run.started", run_id=run.id)
                        self.redis.hset(self.cache_key, run.id, "")

                        command = self.__build_command(process_id, run)
                        self.queue.put(command)

                    for run in runs["stopped"]:
                        self.logger.info("run.stopped", run_id=run.id)
                        self.redis.hdel(self.cache_key, run.id)

            except riffyn.rest.ApiException as err:
                self.logger.error(
                    "runs.poll.failed", status=err.status, error=err.reason
                )

            except Exception as err:
                self.logger.error("runs.poll.failed", error=err)
                raise

            finally:
                self.logger.info("runs.poll.finished")
                self.done.wait(self.poll_interval)
