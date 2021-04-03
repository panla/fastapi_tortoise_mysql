from fastapi import FastAPI

from apps.libs.log import set_logger_handle
from apps.libs.database import init_db
from apps.libs.router import init_router
from apps.libs.exception import register_exception
from apps.libs.middleare import register_cross


def init_app(app: FastAPI):
    set_logger_handle(app)
    init_db(app)
    init_router(app)
    register_exception(app)
    register_cross(app)
