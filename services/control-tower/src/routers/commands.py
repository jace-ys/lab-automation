import typing

from redis import Redis
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, validator
from fastapi.responses import Response

from lib.logger import Logger
from src.commands.command import Command
from src.commands.publisher import CommandPublisher
from src.config import config

cfg = config.Config()
logger = Logger.new()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)
publisher = CommandPublisher(logger, redis, None, None)

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
        return Response(status_code=status.HTTP_201_CREATED)

    except Exception as err:
        raise HTTPException(status_code=500, detail="failed to publish command")
