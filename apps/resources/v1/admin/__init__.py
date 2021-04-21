from fastapi import FastAPI

from . import car
from . import question
from . import token
from . import order


def register_routers(app: FastAPI):
    app.include_router(token.router, prefix='/tokens', tags=['tokens'])
    app.include_router(car.router, prefix='/cars', tags=['cars'])
    app.include_router(question.router, prefix='/questions', tags=['questions'])
    app.include_router(order.router, prefix='/orders', tags=['orders'])
