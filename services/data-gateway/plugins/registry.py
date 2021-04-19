import glob
import importlib


class Pusher:
    def push(self, uuid, rows):
        return NotImplemented


def load(logger):
    plugins = list(
        map(
            lambda path: path.replace("/", ".")[:-3],
            glob.glob("plugins/**/pusher.py"),
        )
    )

    pushers = {}
    for plugin in plugins:
        module = importlib.import_module(plugin)
        pushers[plugin] = module.Pusher(logger)

    return pushers
