from fastapi import FastAPI

from apps.libs.init_app import init_app


def create_app():
    app = FastAPI()

    init_app(app)

    return app
