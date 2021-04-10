import glob
import os
import threading
import typing

import requests

from src.forwarder.payload import Data, DataRow


class BatchForwarder(threading.Thread):
    def __init__(self, logger, manager, cache, cfg, done):
        super(BatchForwarder, self).__init__()

        self.logger = logger
        self.manager = manager
        self.cache = cache
        self.done = done
        self.cache_key = cfg.CACHE_KEY
        self.check_interval = cfg.CHECK_INTERVAL
        self.data_dir = cfg.DATA_DIR
        self.data_gateway_addr = cfg.DATA_GATEWAY_ADDR

    def run(self):
        while not self.done.is_set():
            self.logger.info("batch.poll.started")

            for csv in glob.glob(f"{self.data_dir}/*.csv"):
                try:
                    filename = os.path.basename(csv)
                    diff = self.__diff(filename)
                    if diff:
                        try:
                            uuid = self.manager.get(filename)
                        except ValueError:
                            continue  # No-op

                        count = len(diff)
                        self.logger.info(
                            "batch.forward.started", file=filename, rows=count
                        )

                        rows = list(map(lambda row: DataRow(Data(row)), diff))
                        self.__forward(uuid, rows)
                        self.__seek(filename, count)

                        self.logger.info(
                            "batch.forward.finished", file=filename, rows=count
                        )

                except Exception as err:
                    self.logger.error("batch.forward.failed", file=filename, error=err)

            self.logger.info("batch.poll.finished")
            self.done.wait(self.check_interval)

    def __diff(self, filename):
        with open(f"{self.data_dir}/{filename}", "r") as f:
            lines = f.read().splitlines()[1:]

        position = self.cache.hget(self.cache_key, filename) or 0
        return lines[int(position) :]

    def __forward(self, uuid, rows: typing.List[DataRow]):
        resp = requests.post(
            f"http://{self.data_gateway_addr}/data/batch",
            json={
                "uuid": uuid,
                "rows": list(map(lambda row: vars(row), rows)),
            },
        )
        resp.raise_for_status()

    def __seek(self, filename, count):
        self.cache.hincrby(self.cache_key, filename, count)
