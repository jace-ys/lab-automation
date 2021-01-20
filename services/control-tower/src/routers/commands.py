import typing

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, validator
from fastapi.responses import Response

from lib import log, redis
from src.commands.command import Command
from src.commands.publisher import CommandPublisher
from src.config import config

cfg = config.Config()
logger = log.Logger.new()
pubsub = redis.PubSub.connect(cfg.pubsub.CONNECTION_URL)
publisher = CommandPublisher(logger, pubsub)

router = APIRouter()


class CommandRequest(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[str, typing.Any]

    @validator("spec")
    def spec_not_empty(cls, v):
        if not v:
            raise ValueError("spec must not be empty")
        return v


@router.post("/commands")
async def command(req: CommandRequest):
    try:
        cmd = Command(req.apiVersion, req.protocol, req.spec)
        publisher.publish(cmd)
        logger.info("command.published", command=cmd)

        return Response(status_code=status.HTTP_201_CREATED)

    except Exception as err:
        logger.error("command.publish.failed", command=cmd, error=err)
        raise HTTPException(status_code=500, detail="failed to publish command")
