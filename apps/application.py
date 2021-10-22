from fastapi import FastAPI

from config import Config
from apps.libs import init_app


def create_app():
    app = FastAPI(include_in_schema=Config.INCLUDE_IN_SCHEMA)

    app = init_app(app)

    return app