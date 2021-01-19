from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from lib.logger import Logger
from plugins.riffyn.pusher import Pusher

logger = Logger.new()

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
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


class DataBatchPayload(BaseModel):
    uuid: str
    data: List[Dict[Any, Any]]


@router.post("/data/batch")
async def receive_batch(payload: DataBatchPayload):
    try:
        pusher.push(payload)
        return status.HTTP_202_ACCEPTED

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
