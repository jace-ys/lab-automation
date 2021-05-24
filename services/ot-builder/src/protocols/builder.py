import importlib
import io
import json

from opentrons import simulate


class Build(dict):
    def __init__(self, trigger):
        # Add an empty config object to the trigger
        super(Build, self).__init__(
            {
                "config": {},
                **trigger,
            }
        )


class ProtocolBuilder:
    def __init__(self, logger, cache, cfg):
        self.logger = logger
        self.cache = cache
        self.cache_key = cfg.CACHE_KEY

    def handle_trigger(self, trigger):
        try:
            # Create a build and store it in the cache
            build = Build(trigger)
            self.create(build)
            self.logger.info(
                "build.created", uuid=build["uuid"], protocol=build["protocol"]
            )

        except Exception as err:
            self.logger.error("build.failed", uuid=trigger["uuid"], error=err)

    def list(self):
        # TODO: Order builds by creation time
        builds = self.cache.hgetall(self.cache_key)
        return [json.loads(build) for build in builds.values()]

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
        self.cache.hdel(self.cache_key, build_id)

    def protocol(self, build):
        # Import the protocol definition
        return importlib.import_module(f"src.protocols.{build['protocol']}.protocol")

    def config(self, build):
        # Import the protocol config schema
        return importlib.import_module(
            f"src.protocols.{build['protocol']}.config"
        ).Config.schema()

    def simulate_protocol(self, build):
        # Simulate the protocol and return the execution logs
        protocol_file = self.build_protocol(build)
        runlog, _ = simulate.simulate(io.StringIO(protocol_file))
        return simulate.format_runlog(runlog)

    def build_protocol(self, build):
        # Append the build spec and config to the protocol definition
        with open(f"src/protocols/{build['protocol']}/protocol.py", "r") as f:
            protocol_file = f"""
spec = {build["spec"]}
config = {build["config"]}

{f.read()}
"""
        return protocol_file
