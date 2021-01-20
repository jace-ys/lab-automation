from typing import Any, Dict, List

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel

from lib import log
from plugins.riffyn.pusher import Pusher

logger = log.Logger.new()
pusher = Pusher(logger)

router = APIRouter()


class DataPayload(BaseModel):
    uuid: str
    data: Dict[Any, Any]


@router.post("/data")
async def push_data(payload: DataPayload):
    try:
        pusher.push(payload)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to push data: {str(err)}",
        )


class DataBatchPayload(BaseModel):
    uuid: str
    data: List[Dict[Any, Any]]


@router.post("/data/batch")
async def push_data_batch(payload: DataBatchPayload):
    try:
        pusher.push(payload)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to push data: {str(err)}",
        )
