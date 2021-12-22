__all__ = [
    'init_sub_app',
]

from fastapi import FastAPI

from config import ServiceConfig
from apps.libs import register_exception

from .resources import router


def register_routers(app: FastAPI):
    """register routers"""

    app.include_router(router, tags=['tests'])


def init_sub_app(app: FastAPI):
    """mount sub app"""

    api_app: FastAPI = FastAPI(include_in_schema=ServiceConfig.INCLUDE_IN_SCHEMA)

    register_exception(api_app)
    register_routers(api_app)
    app.mount(path='/api/test', app=api_app, name='api_test_app')

    return app
