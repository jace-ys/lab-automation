import threading

import uvicorn
from fastapi import FastAPI, Request, status
from redis import Redis

from lib import logger
from src.config import config
from src.routers import data

cfg = config.Config()
logger = logger.Logger().get()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)

app = FastAPI()
app.include_router(data.router)


if __name__ == "__main__":
    try:
        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    except KeyboardInterrupt:
        pass

    finally:
        pass
