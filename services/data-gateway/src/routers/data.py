import typing

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel

from lib import log
from plugins import pushers
from plugins.riffyn.pusher import Pusher

logger = log.Logger.new()
pushers = pushers.load(logger)

router = APIRouter()


class DataRow(BaseModel):
    data: typing.Dict[typing.Any, typing.Any]
    well: typing.Union[None, int]


class DataPushRequest(BaseModel):
    uuid: str
    row: DataRow


@router.post("/data")
async def push_data(req: DataPushRequest):
    for plugin, pusher in pushers.items():
        try:
            pusher.push(req)

        except Exception:
            pass

    return Response(status_code=status.HTTP_202_ACCEPTED)


class DataBatchPushRequest(BaseModel):
    uuid: str
    rows: typing.List[DataRow]


@router.post("/data/batch")
async def push_data_batch(req: DataBatchPushRequest):
    for plugin, pusher in pushers.items():
        try:
            pusher.push(req)

        except Exception:
            pass

    return Response(status_code=status.HTTP_202_ACCEPTED)
