import glob
import importlib
import threading
from queue import Queue

import uvicorn
from fastapi import FastAPI

from lib import log, redis
from src.triggers.publisher import TriggerPublisher
from src.config import config
from src.routers import triggers

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.URL)
pubsub = redis.Client.connect(cfg.pubsub.URL)
queue = Queue()

app = FastAPI()
app.include_router(triggers.router)


if __name__ == "__main__":
    done = threading.Event()
    publisher = TriggerPublisher(logger, cache, pubsub, cfg.publisher, queue, done)
    watchers = {}

    try:
        publisher.start()
        logger.info("trigger.publisher.started")

        plugins = list(
            map(
                lambda path: path.replace("/", ".")[:-3],
                glob.glob("plugins/**/watcher.py"),
            )
        )

        for plugin in plugins:
            module = importlib.import_module(plugin)
            watcher = module.Watcher(logger, cache, queue, done)
            watcher.start()
            logger.info(f"{plugin}.started")
            watchers[plugin] = watcher

        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    except KeyboardInterrupt:
        pass

    finally:
        done.set()

        publisher.join()
        logger.info("trigger.publisher.stopped")

        for plugin, watcher in watchers.items():
            watcher.join()
            logger.info(f"{plugin}.stopped")
