from typing import Any, Dict, List

from fastapi import APIRouter, status
from pydantic import BaseModel

from lib import logger
from plugins.riffyn.pusher import Pusher

logger = logger.Logger().get()

router = APIRouter()
pusher = Pusher(logger)


class DataPayload(BaseModel):
    uuid: str
    data: Dict[Any, Any]


@router.post("/data")
async def receive_data(payload: DataPayload):
    try:
        pusher.push(payload)
        return status.HTTP_202_ACCEPTED

    except Exception as err:
        logger.error("data.push.failed", error=err)


class DataBatchPayload(BaseModel):
    uuid: str
    data: List[Dict[Any, Any]]


@router.post("/data/batch")
async def receive_batch(payload: DataBatchPayload):
    try:
        pusher.push(payload)
        return status.HTTP_202_ACCEPTED

    except Exception as err:
        logger.error("data.push.failed", error=err)
