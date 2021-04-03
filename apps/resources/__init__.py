from fastapi import FastAPI

from . import car


def register_routers(app: FastAPI):
    app.include_router(car.router, prefix='/api/v1', tags=['cars'])
