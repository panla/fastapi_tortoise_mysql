__all__ = [
    'init_sub_app',
]

from fastapi import FastAPI

from config import Config
from apps.libs import register_exception

from .resources import router

api_test_app: FastAPI = FastAPI(include_in_schema=Config.INCLUDE_IN_SCHEMA)


def register_routers(app: FastAPI):
    """register routers"""

    app.include_router(router, prefix='/tests', tags=['tests'])


def init_sub_app(app: FastAPI):
    """mount sub app"""

    register_exception(api_test_app)
    register_routers(api_test_app)
    app.mount(path='/api/admin', app=api_test_app, name='api_test_app')

    return app
