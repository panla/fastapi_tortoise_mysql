from fastapi import FastAPI

from config import ServiceConfig
from apps.libs import init_app


def create_app() -> FastAPI:
    app = FastAPI(include_in_schema=ServiceConfig.INCLUDE_IN_SCHEMA)

    app = init_app(app)

    return app
