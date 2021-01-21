import json


class SystemManager:
    def __init__(self, logger, cache, cfg):
        self.logger = logger
        self.cache = cache
        self.cache_key = cfg.CACHE_KEY

    def handle_command(self, command):
        self.cache.hset(self.cache_key, "data/test.csv", json.dumps(command))

    def get_command(self, filename):
        command = self.cache.hget(self.cache_key, filename)
        if command is None:
            raise ValueError(f"could not find managed file: {filename}")

        return json.loads(command)
