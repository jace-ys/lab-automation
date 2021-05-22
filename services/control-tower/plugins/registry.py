import glob
import importlib
import threading


class Watcher(threading.Thread):
    def __init__(self, logger, cache, queue, done):
        super(Watcher, self).__init__()
        return NotImplemented

    def run(self):
        return NotImplemented


def load(logger, cache, queue, done):
    plugins = list(
        map(
            lambda path: path.replace("/", ".")[:-3],
            glob.glob("plugins/**/watcher.py"),
        )
    )

    watchers = {}
    for plugin in plugins:
        module = importlib.import_module(plugin)
        watchers[plugin] = module.Watcher(logger, cache, queue, done)

    return watchers
