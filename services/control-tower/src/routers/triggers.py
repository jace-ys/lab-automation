import typing

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel, validator

from lib import log, redis
from src.triggers import trigger
from src.triggers.publisher import TriggerPublisher
from src.config import config

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.URL)
pubsub = redis.Client.connect(cfg.pubsub.URL)
publisher = TriggerPublisher(logger, cache, pubsub, cfg.publisher)

router = APIRouter()


class GetTriggerResponse(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[typing.Any, typing.Any]
    metadata: typing.Dict[typing.Any, typing.Any]


@router.get("/triggers/{uuid}")
async def get_trigger(uuid: str):
    try:
        trg = publisher.get(uuid)
        return trg

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"failed to get trigger: {str(err)}",
        )


class PublishTriggerRequest(BaseModel):
    apiVersion: str
    protocol: str
    spec: typing.Dict[typing.Any, typing.Any]

    @validator("spec")
    def spec_not_empty(cls, v):
        if not v:
            raise ValueError("spec must not be empty")

        return v


@router.post("/triggers")
async def publish_trigger(req: PublishTriggerRequest):
    try:
        trg = trigger.Trigger(req.apiVersion, req.protocol, req.spec)
        trg.metadata("service.control-tower.api", {"endpoint": "/triggers"})
        publisher.publish(trg)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except trigger.InvalidAPIVersion:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to publish trigger: invalid API version",
        )

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to publish trigger: {str(err)}",
        )
