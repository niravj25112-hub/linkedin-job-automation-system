from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        version="0.1.0",
        description="Recruitment automation API for job discovery, resume matching, email outreach, and submission tracking.",
    )
    app.include_router(api_router, prefix=settings.api_v1_prefix)
    return app


app = create_app()

