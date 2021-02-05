import json

import requests

from src.config import config
from src.forwarder.basic import BasicForwarder
from src.forwarder.payload import DataRow

cfg = config.Config()
forwarder = BasicForwarder(cfg.forwarder)


class ConfigureError(BaseException):
    pass


class Experiment:
    def __init__(self, uuid, csv):
        self.uuid = uuid
        self.csv = csv


class SystemManager:
    def __init__(self, logger, cache, cfg):
        self.logger = logger
        self.cache = cache
        self.cache_key = cfg.CACHE_KEY
        self.chibio_server_addr = cfg.CHIBIO_SERVER_ADDR

    def handle_command(self, command):
        try:
            device = self.__configure_experiment(command)
            experiment_id = self.__create_experiment(device)
            csv = f"{experiment_id}_data.csv"

            experiment = Experiment(command["uuid"], csv)
            self.create(experiment)
            self.logger.info("experiment.created", uuid=experiment.uuid)

        except ConfigureError as err:
            self.logger.error(
                "experiment.create.failed", uuid=command["uuid"], error=err
            )

            try:
                data = DataRow()
                data.error = str(err)
                forwarder.forward(command["uuid"], vars(data))
                self.logger.info("configure.error.forwarded", uuid=command["uuid"])

            except Exception as err:
                self.logger.error(
                    "configure.error.forward.failed", uuid=command["uuid"], error=err
                )

        except Exception as err:
            self.logger.error(
                "experiment.create.failed", uuid=command["uuid"], error=err
            )

    def create(self, experiment):
        self.cache.hset(self.cache_key, experiment.csv, experiment.uuid)

    def get(self, csv):
        uuid = self.cache.hget(self.cache_key, csv)
        if uuid is None:
            raise ValueError(f"could not find managed CSV file: {csv}")

        return uuid

    def __configure_experiment(self, command):
        if "metadata" in command:
            source = command["metadata"]["source"]["name"]
        else:
            source = command["uuid"]

        chibio = command["spec"]["chibio"]
        data = {}

        # TODO: Handle more cases
        if "od" in chibio:
            data["OD"] = {"target": chibio["od"]}

        if "volume" in chibio:
            data["Volume"] = {"target": chibio["volume"]}

        if "thermostat" in chibio:
            data["Thermostat"] = {"target": chibio["thermostat"]}

        resp = requests.post(
            f"http://{self.chibio_server_addr}/sysData",
            json={
                "source": source,
                "device": {"M": chibio["devicePosition"], "name": chibio["deviceName"]},
                "sysData": data,
            },
        )

        if resp.status_code == 422:
            body = resp.json()
            raise ConfigureError(body["error"])
        else:
            resp.raise_for_status()

        body = resp.json()
        return body["device"]["M"]

    def __create_experiment(self, device):
        resp = requests.post(f"http://{self.chibio_server_addr}/Experiment/{device}")
        resp.raise_for_status()

        body = resp.json()
        return body["experimentID"]
