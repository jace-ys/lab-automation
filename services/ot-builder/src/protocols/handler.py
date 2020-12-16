import json
import uuid

import jinja2
from jinja2 import meta


class ProtocolHandler:
    def __init__(self, logger, redis, api_version):
        self.logger = logger
        self.redis = redis
        self.api_version = api_version

    def receive(self, message):
        if message["type"] != "message":
            return

        command = json.loads(message["data"])
        self.logger.info("command.received", protocol=command["protocol"])

        run = command
        self.redis.hset(self.api_version, run["uuid"], json.dumps(run))
        self.logger.info("run.created", id=run["uuid"])

    def build(self, protocol, spec):
        f = open(f"src/protocols/{protocol}/protocol.py", "r").read()

        protocol_file = f"""
spec = {spec}

{f}
"""

        return protocol_file
