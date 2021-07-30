__all__ = [
    'init_sub_app',
]

from fastapi import FastAPI

from config import Config
from apps.libs import register_exception

from .resources import car
from .resources import file
from .resources import order
from .resources import question
from .resources import token
from .resources import user
from .resources import test

v1_admin_app: FastAPI = FastAPI(include_in_schema=Config.INCLUDE_IN_SCHEMA)


def register_routers(app: FastAPI):
    """register routers"""

    app.include_router(car.router, prefix='/cars', tags=['cars'])
    app.include_router(file.router, prefix='/files', tags=['files'])
    app.include_router(order.router, prefix='/orders', tags=['orders'])
    app.include_router(question.router, prefix='/questions', tags=['questions'])
    app.include_router(token.router, prefix='/tokens', tags=['tokens'])
    app.include_router(user.router, prefix='/users', tags=['users'])
    app.include_router(test.router, prefix='/tests', tags=['tests'])

def init_sub_app(app: FastAPI):
    """mount sub app"""

    register_exception(v1_admin_app)
    register_routers(v1_admin_app)
    app.mount(path='/api/v1/admin', app=v1_admin_app, name='v1_admin_app')
