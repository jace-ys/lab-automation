import threading
from queue import Queue

import uvicorn
from fastapi import FastAPI

from lib import log, redis
from plugins import registry
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
    watchers = registry.load(logger, cache, queue, done)

    try:
        publisher.start()
        logger.info("trigger.publisher.started")

        for plugin, watcher in watchers.items():
            watcher.start()
            logger.info(f"{plugin}.started")

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
