from fastapi import FastAPI

from . import car
from . import question


def register_routers(app: FastAPI):
    app.include_router(car.router, prefix='/cars', tags=['cars'])
    app.include_router(question.router, prefix='/questions', tags=['questions'])
