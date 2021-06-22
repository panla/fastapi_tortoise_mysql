from fastapi import FastAPI

from . import car
from . import file
from . import order
from . import question
from . import token
from . import user

def register_routers(app: FastAPI):
    """注册路由"""

    app.include_router(car.router, prefix='/cars', tags=['cars'])
    app.include_router(file.router, prefix='/files', tags=['files'])
    app.include_router(order.router, prefix='/orders', tags=['orders'])
    app.include_router(question.router, prefix='/questions', tags=['questions'])
    app.include_router(token.router, prefix='/tokens', tags=['tokens'])
    app.include_router(user.router, prefix='/users', tags=['users'])
