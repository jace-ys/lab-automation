import importlib
import io
import json

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from opentrons import simulate

from lib.logger import Logger
from src.config import config
from src.protocols.handler import ProtocolHandler

cfg = config.Config()
logger = Logger.new()

redis = Redis(host=cfg.redis.HOST, port=cfg.redis.PORT, decode_responses=True)
views = Jinja2Templates(directory=cfg.server.VIEWS_DIR)
protocol_handler = ProtocolHandler(logger, redis, cfg.API_VERSION)

router = APIRouter()


def list_runs():
    runs = redis.hgetall(cfg.API_VERSION)
    runs = [json.loads(v) for k, v in runs.items()]

    return runs


def get_run(run_id):
    run = redis.hget(cfg.API_VERSION, run_id)
    if run is None:
        raise ValueError(f"could not find run with UUID {run_id}")

    return json.loads(run)


def update_run(run_id, run):
    updated = redis.hset(cfg.API_VERSION, run_id, json.dumps(run))

    return run


def parse_form(form_data, schema):
    spec = {}

    for key, value in form_data.items():
        nested = spec
        local = schema.spec["local"]

        parts = key.split(".")
        for i, part in enumerate(parts):
            local = local[part]

            if i < len(parts) - 1:
                nested = nested.setdefault(part, {})
            else:
                if local["type"] == "location":
                    nested.setdefault(part, int(value))
                else:
                    nested.setdefault(part, value)

    return spec


def run_simulation(protocol_file):
    run_log, _bundle = simulate.simulate(io.StringIO(protocol_file))
    return simulate.format_runlog(run_log)


@router.get("/runs")
async def handle_list_runs(request: Request):
    try:
        runs = list_runs()

        logger.info("run.list.success")
        return views.TemplateResponse(
            "runs/list.html",
            {
                "request": request,
                "runs": runs,
            },
        )

    except Exception as err:
        logger.info("runs.list.failed", error=err)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,  # TODO: Inspect error to return different error messages
            },
        )


@router.get("/runs/{run_id}")
async def handle_get_run(request: Request, run_id: str):
    try:
        run = get_run(run_id)
        schema = importlib.import_module(f"src.protocols.{run['protocol']}.schema")

        logger.info("run.get.success", run_id=run_id)
        return views.TemplateResponse(
            "runs/get.html",
            {
                "request": request,
                "run": run,
                "local": schema.Schema().spec["local"],
            },
        )

    except Exception as err:
        logger.info("run.get.failed", error=err, run_id=run_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.delete("/runs/{run_id}")
async def handle_delete_run(request: Request, run_id: str):
    # TODO: Delete runs after a certain time
    pass


@router.get("/runs/{run_id}/download")
async def handle_download(request: Request, run_id: str):
    try:
        run = get_run(run_id)

        protocol_file = protocol_handler.build(run["protocol"], run["spec"])
        headers = {
            "Content-Disposition": f"attachment; filename={run['protocol']}_{run['uuid']}.py"
        }

        logger.info("download.success", run_id=run_id)
        return StreamingResponse(io.StringIO(protocol_file), headers=headers)

    except Exception as err:
        logger.info("download.failed", error=err, run_id=run_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.post("/runs/{run_id}/download")
async def handle_update_download(request: Request, run_id: str):
    try:
        run = get_run(run_id)
        schema = importlib.import_module(f"src.protocols.{run['protocol']}.schema")

        form_data = await request.form()
        spec = parse_form(form_data, schema.Schema())

        run["spec"] = {**run["spec"], **spec}
        run = update_run(run_id, run)

        logger.info("download.update.success", run_id=run_id)
        return RedirectResponse(
            url=f"/runs/{run_id}/download", status_code=status.HTTP_303_SEE_OTHER
        )

    except Exception as err:
        logger.info("download.update.failed", error=err, run_id=run_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.get("/runs/{run_id}/simulate")
async def handle_simulate(request: Request, run_id: str):
    try:
        run = get_run(run_id)

        protocol_file = protocol_handler.build(run["protocol"], run["spec"])
        simulation = run_simulation(protocol_file)

        logger.info("simulate.success", run_id=run_id)
        return views.TemplateResponse(
            "runs/simulate.html",
            {
                "request": request,
                "run": run,
                "simulation": simulation,
            },
        )

    except Exception as err:
        logger.info("simulate.failed", error=err, run_id=run_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.post("/runs/{run_id}/simulate")
async def handle_update_simulate(request: Request, run_id: str):
    try:
        run = get_run(run_id)
        schema = importlib.import_module(f"src.protocols.{run['protocol']}.schema")

        form_data = await request.form()
        spec = parse_form(form_data, schema.Schema())

        run["spec"] = {**run["spec"], **spec}
        run = update_run(run_id, run)

        logger.info("simulate.update.success", run_id=run_id)
        return RedirectResponse(
            url=f"/runs/{run_id}/simulate", status_code=status.HTTP_303_SEE_OTHER
        )

    except Exception as err:
        logger.info("simulate.update.failed", error=err, run_id=run_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )
