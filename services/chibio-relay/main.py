import threading

import uvicorn
from fastapi import FastAPI

from lib import api, log, redis
from lib.commands.subscriber import Subscriber
from src.config import config
from src.forwarder.batch import BatchForwarder
from src.system.manager import SystemManager

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.URL)
pubsub = redis.Client.connect(cfg.pubsub.URL).pubsub()

app = FastAPI()


if __name__ == "__main__":
    done = threading.Event()

    manager = SystemManager(logger, cache, cfg.manager)
    forwarder = BatchForwarder(logger, manager, cache, cfg.forwarder, done)
    subscriber = Subscriber(manager)
    topic = api.device(cfg.version, cfg.manager.DEVICE_NAME)

    try:
        pubsub.subscribe(**{topic: subscriber.receive})
        # TODO: Handle exception in thread using https://github.com/andymccurdy/redis-py/pull/1395
        pubsub_thread = pubsub.run_in_thread()
        logger.info("manager.subscribe.started", topic=topic)

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
        logger.info("manager.subscribe.stopped")

        forwarder.join()
        logger.error("data.forwarder.stopped")
