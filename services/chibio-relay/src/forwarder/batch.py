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
        self.data_gateway_url = cfg.DATA_GATEWAY_URL

    def run(self):
        # Keep polling until a done signal is received
        while not self.done.is_set():
            self.logger.info("batch.poll.started")

            # Find all CSV files in the data directory
            for csv in glob.glob(f"{self.data_dir}/*.csv"):
                try:
                    # Get the name of the CSV file
                    filename = os.path.basename(csv)
                    # Check if any additional data has been written since we last read
                    diff = self.__diff(filename)
                    if diff:
                        # Check if this is a file associated with an active experiment
                        try:
                            uuid = self.manager.get(filename)
                        except ValueError:
                            continue  # No-op

                        count = len(diff)
                        self.logger.info(
                            "batch.forward.started", file=filename, rows=count
                        )

                        # Forward the data and increment the read cursor
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
        # Read the CSV and split it by lines
        with open(f"{self.data_dir}/{filename}", "r") as f:
            lines = f.read().splitlines()[1:]

        # Check which line we last read the file until and return any new lines
        position = self.cache.hget(self.cache_key, filename) or 0
        return lines[int(position) :]

    def __forward(self, uuid, rows: typing.List[DataRow]):
        # Forward the data to the service.date-gateway
        resp = requests.post(
            f"{self.data_gateway_url}/data/batch",
            json={
                "uuid": uuid,
                "rows": list(map(lambda row: vars(row), rows)),
            },
        )
        resp.raise_for_status()

    def __seek(self, filename, count):
        self.cache.hincrby(self.cache_key, filename, count)
