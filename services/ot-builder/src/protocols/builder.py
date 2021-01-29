import importlib
import io
import json

from opentrons import simulate


class Build(dict):
    def __init__(self, command):
        config = {"config": {}}
        super(Build, self).__init__({**command, **config})


class ProtocolBuilder:
    def __init__(self, logger, cache, cfg):
        self.logger = logger
        self.cache = cache
        self.cache_key = cfg.CACHE_KEY

    def handle_command(self, command):
        try:
            build = Build(command)
            self.create(build)
            self.logger.info(
                "build.created", uuid=build["uuid"], protocol=build["protocol"]
            )

        except Exception as err:
            self.logger.error("build.failed", uuid=command["uuid"], error=err)

    def list(self):
        # TODO: Order builds by creation time
        builds = self.cache.hgetall(self.cache_key)
        return [json.loads(v) for k, v in builds.items()]

    def get(self, build_id):
        build = self.cache.hget(self.cache_key, build_id)
        if build is None:
            raise ValueError(f"could not find build with UUID {build_id}")

        return json.loads(build)

    def create(self, build):
        self.cache.hset(self.cache_key, build["uuid"], json.dumps(build))

    def update(self, build_id, build):
        self.cache.hset(self.cache_key, build_id, json.dumps(build))

    def delete(self, build_id):
        # TODO
        pass

    def config(self, build):
        return importlib.import_module(
            f"src.protocols.{build['protocol']}.config"
        ).Config.schema()

    def simulate_protocol(self, build):
        protocol_file = self.build_protocol(build)
        runlog, _ = simulate.simulate(io.StringIO(protocol_file))
        return simulate.format_runlog(runlog)

    def build_protocol(self, build):
        with open(f"src/protocols/{build['protocol']}/protocol.py", "r") as f:
            protocol_file = f"""spec = {build["spec"]}
config = {build["config"]}

{f.read()}
"""
        return protocol_file
