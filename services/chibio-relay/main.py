import threading

import uvicorn
from fastapi import FastAPI

from lib import log, redis
from src.config import config
from src.forwarder.batch import BatchForwarder

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.CONNECTION_URL)

app = FastAPI()


if __name__ == "__main__":
    done = threading.Event()
    forwarder = BatchForwarder(logger, cache, done, cfg.forwarder)

    try:
        forwarder.start()
        logger.error("data.forwarder.started")

        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    except KeyboardInterrupt:
        pass

    finally:
        done.set()

        forwarder.join()
        logger.error("data.forwarder.stopped")
