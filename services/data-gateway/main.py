import uvicorn
from fastapi import FastAPI

from lib import log
from src.config import config
from src.routers import data

cfg = config.Config()
logger = log.Logger.new()

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
