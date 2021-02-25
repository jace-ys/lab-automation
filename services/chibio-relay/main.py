import threading

import uvicorn
from fastapi import FastAPI

from lib import log, redis
from lib.commands.subscriber import Subscriber
from src.config import config
from src.forwarder.batch import BatchForwarder
from src.system.manager import SystemManager

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.ADDR)
pubsub = redis.Client.connect(cfg.pubsub.ADDR).pubsub()

app = FastAPI()


if __name__ == "__main__":
    done = threading.Event()

    manager = SystemManager(logger, cache, cfg.manager)
    forwarder = BatchForwarder(logger, manager, cache, cfg.forwarder, done)
    subscriber = Subscriber(manager)

    try:
        pubsub.subscribe(**{cfg.pubsub.SUBSCRIPTION_TOPIC: subscriber.receive})
        pubsub_thread = pubsub.run_in_thread()  # TODO: Handle exception in thread
        logger.info("pubsub.listen.started", channel=cfg.pubsub.SUBSCRIPTION_TOPIC)

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

        pubsub_thread.stop()
        logger.info("pubsub.listen.stopped")

        forwarder.join()
        logger.error("data.forwarder.stopped")
