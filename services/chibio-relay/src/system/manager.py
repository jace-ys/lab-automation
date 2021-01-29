import json

import requests


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
            device = self.__configure_chibio(command)
            csv = self.__start_chibio(device)

            experiment = Experiment(command["uuid"], csv)
            self.create(experiment)
            self.logger.info("experiment.created", uuid=experiment.uuid)

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

    def __configure_chibio(self, command):
        if "metadata" in command:
            source = command["metadata"]["source"]["name"]
        else:
            source = command["uuid"]

        spec = command["spec"]
        data = {}

        # TODO: Handle more cases
        if "thermostat" in spec:
            data["Thermostat"] = {"target": spec["thermostat"]["temperature"]}

        if "leds" in spec:
            if "395Nm" in spec["leds"]:
                data["LEDA"] = {"target": spec["leds"]["395Nm"]}

        resp = requests.post(
            f"http://{self.chibio_server_addr}/sysData",
            json={"source": source, "data": data},
        )
        resp.raise_for_status()

        body = resp.json()
        return body["device"]

    def __start_chibio(self, device):
        resp = requests.post(f"http://{self.chibio_server_addr}/Experiment/1/{device}")
        resp.raise_for_status()

        body = resp.json()
        return body["csv_filename"]
