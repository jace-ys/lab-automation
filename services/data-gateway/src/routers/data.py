import typing

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel

from lib import log
from plugins.riffyn.pusher import Pusher

logger = log.Logger.new()
pusher = Pusher(logger)

router = APIRouter()


class DataPushRequest(BaseModel):
    uuid: str
    data: typing.Dict[typing.Any, typing.Any]


@router.post("/data")
async def push_data(req: DataPushRequest):
    try:
        pusher.push(req)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to push data: {str(err)}",
        )


class DataBatchPushRequest(BaseModel):
    uuid: str
    data: typing.List[typing.Dict[typing.Any, typing.Any]]


@router.post("/data/batch")
async def push_data_batch(req: DataBatchPushRequest):
    try:
        pusher.push(req)
        return Response(status_code=status.HTTP_202_ACCEPTED)

    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"failed to push data: {str(err)}",
        )
