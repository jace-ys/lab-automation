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
pubsub = redis.Client.connect(cfg.pubsub.CONNECTION_URL)
publisher = CommandPublisher(logger, pubsub)

router = APIRouter()


class CommandPayload(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[str, typing.Any]

    @validator("spec")
    def spec_not_empty(cls, v):
        if not v:
            raise ValueError("spec must not be empty")

        return v


@router.post("/commands")
async def publish_command(payload: CommandPayload):
    try:
        cmd = command.Command(payload.apiVersion, payload.protocol, payload.spec)
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
