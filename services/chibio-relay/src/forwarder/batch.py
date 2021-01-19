import glob
import threading

import requests

from src.forwarder.payload import DataRow


class BatchForwarder(threading.Thread):
    def __init__(self, logger, redis, done, cfg):
        super(BatchForwarder, self).__init__()

        self.logger = logger
        self.redis = redis
        self.done = done
        self.check_interval = cfg.CHECK_INTERVAL
        self.data_dir = cfg.DATA_DIR
        self.data_gateway_addr = cfg.SERVICE_DATA_GATEWAY_ADDR

    def run(self):
        while not self.done.is_set():
            self.logger.info("batch.poll.started")

            for f in glob.glob(f"{self.data_dir}/*.csv"):
                try:
                    rows = self.__diff(f)
                    if rows:
                        self.__forward(rows)
                        self.__seek(f, len(rows))

                    self.logger.info("batch.forward.finished", file=f, count=len(rows))

                except Exception as err:
                    self.logger.error("batch.forward.failed", file=f, error=err)
                    raise

            self.done.wait(self.check_interval)

    def __diff(self, csv):
        with open(csv, "r") as f:
            lines = f.read().splitlines()[1:]

        position = self.redis.hget("ChiBio/v1alpha1", csv) or 0
        return lines[int(position) :]

    def __forward(self, rows):
        data = list(map(lambda row: vars(DataRow(row)), rows))
        resp = requests.post(
            f"http://{self.data_gateway_addr}/data/batch",
            json={
                "uuid": "",
                "data": data,
            },
        )
        resp.raise_for_status()

    def __seek(self, csv, rows):
        self.redis.hincrby("ChiBio/v1alpha1", csv, rows)
