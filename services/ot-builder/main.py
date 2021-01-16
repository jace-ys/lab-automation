import uvicorn
from fastapi import FastAPI
from redis import Redis

from lib import logger
from src.config import config
from src.protocols.handler import ProtocolHandler
from src.routers import runs

cfg = config.Config()
logger = logger.Logger().get()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)
pubsub = redis.pubsub()

app = FastAPI()
app.include_router(runs.router)


if __name__ == "__main__":
    handler = ProtocolHandler(logger, redis, cfg.API_VERSION)

    try:
        pubsub.subscribe(**{cfg.API_VERSION: handler.receive})
        pubsub_thread = pubsub.run_in_thread()  # TODO: Handle exception in thread
        logger.info("pubsub.listen.started", channel=cfg.API_VERSION)

        logger.info("server.started", port=cfg.server.PORT)
        uvicorn.run(app, host=cfg.server.HOST, port=cfg.server.PORT)
        logger.info("server.stopped")

    except Exception as err:
        logger.error("service.fatal", error=err)

    except KeyboardInterrupt:
        pass

    finally:
        pubsub_thread.stop()
        logger.info("pubsub.listen.stopped")
