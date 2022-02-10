from fastapi import FastAPI

from config import ServiceConfig
from apps.libs import register_exception

from .endpoints import (
    car, file, order, question,
    token, user, code
    )


def register_routers(app: FastAPI):
    """register routers"""

    app.include_router(car.router, prefix='/cars', tags=['cars'])
    app.include_router(file.router, prefix='/files', tags=['files'])
    app.include_router(order.router, prefix='/orders', tags=['orders'])
    app.include_router(question.router, prefix='/questions', tags=['questions'])
    app.include_router(token.router, prefix='/tokens', tags=['tokens'])
    app.include_router(user.router, prefix='/users', tags=['users'])
    app.include_router(code.router, prefix='/code', tags=['code'])


def init_sub_app(app: FastAPI) -> FastAPI:
    """mount sub app"""

    api_app: FastAPI = FastAPI(include_in_schema=ServiceConfig.INCLUDE_IN_SCHEMA)

    register_exception(api_app)
    register_routers(api_app)
    app.mount(path='/api/admin', app=api_app, name='api_admin_app')

    return app
