import threading

import uvicorn
from fastapi import FastAPI
from redis import Redis

from lib.logger import Logger
from src.config import config
from src.forwarder.batch import BatchForwarder

cfg = config.Config()
logger = Logger.new()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)

app = FastAPI()


if __name__ == "__main__":
    done = threading.Event()
    forwarder = BatchForwarder(logger, redis, done, cfg.forwarder)

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
