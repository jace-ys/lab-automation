import glob
import importlib
import sys
import threading
from queue import Queue

import uvicorn
from fastapi import FastAPI
from redis import Redis

from lib import logger
from src.commands.publisher import CommandPublisher
from src.config import config
from src.routers import commands

cfg = config.Config()
logger = logger.Logger().get()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)
queue = Queue()

app = FastAPI()
app.include_router(commands.router)

if __name__ == "__main__":
    done = threading.Event()
    publisher = CommandPublisher(logger, redis, queue, done)

    try:
        publisher.start()
        logger.info("command.publisher.started")

        plugins = list(
            map(
                lambda path: path.replace("/", ".")[:-1],
                glob.glob("plugins/**/"),
            )
        )

        for plugin in plugins:
            watcher = importlib.import_module(f"{plugin}.watcher").Watcher(
                logger, redis, queue, done
            )
            watcher.start()
            logger.info(f"{plugin}.watcher.started")

        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    finally:
        done.set()

        logger.info("command.publisher.started")

        for plugin in plugins:
            logger.info(f"{plugin}.watcher.stopped")

        sys.exit(1)
