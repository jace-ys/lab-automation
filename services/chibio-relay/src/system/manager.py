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
    FP1_EXCITE = {
        "395/30": "LEDA",
        "457/35": "LEDB",
        "500/55": "LEDC",
        "523/70": "LEDD",
        "595/25": "LEDE",
        "623/30": "LEDF",
        "6500K": "LEDG",
        "Laser": "LASER650",
    }

    FP1_GAIN = {
        "0.5x": "x0",
        "1x": "x1",
        "2x": "x2",
        "4x": "x3",
        "8x": "x4",
        "16x": "x5",
        "32x": "x6",
        "64x": "x7",
        "128x": "x8",
        "256x": "x9",
        "512x": "x10",
    }

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

        spec = command["spec"]
        data = {}

        # TODO: Handle more cases
        if "od" in spec:
            data["OD"] = {"target": spec["od"]}

        if "volume" in spec:
            data["Volume"] = {"target": spec["volume"]}

        if "thermostat" in spec:
            data["Thermostat"] = {"target": spec["thermostat"]}

        if "fp1Excite" in spec:
            data["FP1"] = {"ON": 1}

            led = SystemManager.FP1_EXCITE.get(spec["fp1Excite"])
            if led is None:
                raise ConfigureError(
                    f"invalid value for fp1Excite: {spec['fp1Excite']}"
                )

            data["FP1"].update({"LED": led})

            if "fp1Gain" in spec:
                gain = SystemManager.FP1_GAIN.get(spec["fp1Gain"])
                if gain is None:
                    raise ConfigureError(
                        f"invalid value for fp1gain: {spec['fp1Gain']}"
                    )
            else:
                raise ConfigureError("missing value for fp1Gain")

            data["FP1"].update({"Gain": gain})

        resp = requests.post(
            f"http://{self.chibio_server_addr}/sysData",
            json={
                "source": source,
                "device": {"M": spec["devicePosition"], "name": spec["deviceName"]},
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
