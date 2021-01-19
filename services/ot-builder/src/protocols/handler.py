import json


class ProtocolHandler:
    def __init__(self, logger, redis, api_version):
        self.logger = logger
        self.redis = redis
        self.api_version = api_version

    def receive(self, message):
        if message["type"] != "message":
            return

        try:
            command = json.loads(message["data"])
            self.logger.info("command.received", protocol=command["protocol"])

            self.redis.hset(self.api_version, command["uuid"], message["data"])
            self.logger.info("run.created", id=command["uuid"])

        except Exception as err:
            self.logger.error("run.create.failed", error=err)
            raise

    def build(self, protocol, spec):
        f = open(f"src/protocols/{protocol}/protocol.py", "r").read()

        protocol_file = f"""
spec = {spec}

{f}
"""

        return protocol_file
