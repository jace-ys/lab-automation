import typing

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel, validator

from lib import log, redis
from src.commands import command
from src.commands.publisher import CommandPublisher
from src.config import config

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.CONNECTION_URL)
pubsub = redis.Client.connect(cfg.pubsub.CONNECTION_URL)
publisher = CommandPublisher(logger, cache, pubsub, cfg.publisher)

router = APIRouter()


class GetCommandResponse(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[typing.Any, typing.Any]
    metadata: typing.Dict[typing.Any, typing.Any]


@router.get("/commands/{uuid}")
async def get_command(uuid: str):
    try:
        cmd = publisher.get(uuid)
        return cmd

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"failed to get command: {str(err)}",
        )


class PublishCommandRequest(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[typing.Any, typing.Any]

    @validator("spec")
    def spec_not_empty(cls, v):
        if not v:
            raise ValueError("spec must not be empty")

        return v


@router.post("/commands")
async def publish_command(req: PublishCommandRequest):
    try:
        cmd = command.Command(req.apiVersion, req.protocol, req.spec).with_metadata(
            "service.control-tower.api", {"endpoint": "/commands"}
        )

        publisher.publish(cmd)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except command.InvalidAPIVersion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to publish command: invalid API version",
        )

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to publish command: {str(err)}",
        )
