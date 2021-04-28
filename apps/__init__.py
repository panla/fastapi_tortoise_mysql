from fastapi import FastAPI

import config
from apps.libs.init_app import init_app


def create_app():
    app = FastAPI(include_in_schema=config.include_in_schema)

    init_app(app)

    return app
