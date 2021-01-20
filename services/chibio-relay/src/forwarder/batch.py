import glob
import threading

import requests

from src.forwarder.payload import DataRow


class BatchForwarder(threading.Thread):
    def __init__(self, logger, cache, done, cfg):
        super(BatchForwarder, self).__init__()

        self.logger = logger
        self.cache = cache
        self.done = done
        self.cache_key = cfg.CACHE_KEY
        self.check_interval = cfg.CHECK_INTERVAL
        self.data_dir = cfg.DATA_DIR
        self.data_gateway_addr = cfg.DATA_GATEWAY_ADDR

    def run(self):
        while not self.done.is_set():
            self.logger.info("batch.poll.started")

            for f in glob.glob(f"{self.data_dir}/*.csv"):
                try:
                    rows = self.__diff(f)
                    if rows:
                        count = len(rows)
                        self.logger.info("batch.forward.started", file=f, rows=count)
                        self.__forward(rows)
                        self.__seek(f, count)
                        self.logger.info("batch.forward.finished", file=f, rows=count)

                except Exception as err:
                    self.logger.error("batch.forward.failed", file=f, error=err)
                    raise

            self.logger.info("batch.poll.finished")
            self.done.wait(self.check_interval)

    def __diff(self, csv):
        with open(csv, "r") as f:
            lines = f.read().splitlines()[1:]

        position = self.cache.hget(self.cache_key, csv) or 0
        return lines[int(position) :]

    def __forward(self, rows):
        data = list(map(lambda row: vars(DataRow(row)), rows))
        resp = requests.post(
            f"http://{self.data_gateway_addr}/data/batch",
            json={
                "uuid": "",  # TODO: Use uuid from command
                "data": data,
            },
        )
        resp.raise_for_status()

    def __seek(self, csv, rows):
        self.cache.hincrby(self.cache_key, csv, rows)
