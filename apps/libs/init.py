__all__ = [
    'init_app',
]

from fastapi import FastAPI

from .database import init_db
from .middleware import register_cross, register_middleware

from apps.api_admin import init_sub_app as init_api_admin_app
from apps.api_test import init_sub_app as init_api_test_app
from sockets import init_sub_app as init_socket_io_app


def init_app(app: FastAPI):
    """the entrance to init app"""

    init_db(app)
    register_cross(app)
    register_middleware(app)

    app = init_api_admin_app(app)
    app = init_api_test_app(app)
    app = init_socket_io_app(app)

    return app
