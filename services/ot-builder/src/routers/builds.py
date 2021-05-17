import io

from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse, StreamingResponse
from fastapi.templating import Jinja2Templates

from lib import log, redis
from src.config import config
from src.protocols.builder import ProtocolBuilder

cfg = config.Config()
logger = log.Logger.new()
cache = redis.Client.connect(cfg.cache.URL)
builder = ProtocolBuilder(logger, cache, cfg.builder)

router = APIRouter()
views = Jinja2Templates(directory=cfg.server.VIEWS_DIR)


def parse_form(form_data):
    spec = {}

    for key, value in form_data.items():
        nested = spec
        parts = key.split(".")
        for i, part in enumerate(parts):
            if i < len(parts) - 1:
                nested = nested.setdefault(part, {})
            else:
                if part == "location":
                    nested.setdefault(part, int(value))
                else:
                    nested.setdefault(part, value)

    return spec


@router.get("/builds")
async def handle_list_builds(request: Request):
    try:
        builds = builder.list()

        logger.info("builds.list.success")
        return views.TemplateResponse(
            "builds/list.html",
            {
                "request": request,
                "builds": builds,
            },
        )

    except Exception as err:
        logger.info("builds.list.failed", error=err)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.get("/builds/{build_id}")
async def handle_get_build(request: Request, build_id: str):
    try:
        build = builder.get(build_id)
        protocol = builder.protocol(build)
        config = builder.config(build)

        logger.info("build.get.success", build_id=build_id)
        return views.TemplateResponse(
            "builds/get.html",
            {
                "request": request,
                "build": build,
                "protocol": protocol,
                "config": config,
            },
        )

    except Exception as err:
        logger.info("build.get.failed", error=err, build_id=build_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.get("/builds/{build_id}/download")
async def handle_download_build(request: Request, build_id: str):
    try:
        build = builder.get(build_id)
        protocol_file = builder.build_protocol(build)
        headers = {
            "Content-Disposition": f"attachment; filename={build['protocol']}_{build['uuid']}.py"
        }

        logger.info("download.success", build_id=build_id)
        return StreamingResponse(io.StringIO(protocol_file), headers=headers)

    except Exception as err:
        logger.info("download.failed", error=err, build_id=build_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.post("/builds/{build_id}/download")
async def handle_update_download(request: Request, build_id: str):
    try:
        build = builder.get(build_id)
        form_data = await request.form()
        build["config"] = parse_form(form_data)
        builder.update(build_id, build)

        logger.info("download.update.success", build_id=build_id)
        return RedirectResponse(
            url=f"/builds/{build_id}/download", status_code=status.HTTP_303_SEE_OTHER
        )

    except Exception as err:
        logger.info("download.update.failed", error=err, build_id=build_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.get("/builds/{build_id}/simulate")
async def handle_simulate(request: Request, build_id: str):
    try:
        build = builder.get(build_id)
        simulation = builder.simulate_protocol(build)

        logger.info("simulate.success", build_id=build_id)
        return views.TemplateResponse(
            "builds/simulate.html",
            {
                "request": request,
                "build": build,
                "simulation": simulation,
            },
        )

    except Exception as err:
        logger.info("simulate.failed", error=err, build_id=build_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )


@router.post("/builds/{build_id}/simulate")
async def handle_update_simulate(request: Request, build_id: str):
    try:
        build = builder.get(build_id)
        form_data = await request.form()
        build["config"] = parse_form(form_data)
        builder.update(build_id, build)

        logger.info("simulate.update.success", build_id=build_id)
        return RedirectResponse(
            url=f"/builds/{build_id}/simulate", status_code=status.HTTP_303_SEE_OTHER
        )

    except Exception as err:
        logger.info("simulate.update.failed", error=err, build_id=build_id)
        return views.TemplateResponse(
            "error.html",
            {
                "request": request,
                "error": err,
            },
        )
