__all__ = ['ns_sio', 'sio_server', 'init_sub_app']

import socketio
from fastapi import FastAPI

from .event import NameSpaceSIO
from config import Config
from apps.utils import logger

sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

ns_sio = NameSpaceSIO(namespace=Config.SOCKET_IO_NAMESPACE)

sio_server.register_namespace(ns_sio)


def init_sub_app(app: FastAPI):
    """mount sub app"""

    v1_socket_io_app = socketio.ASGIApp(sio_server, socketio_path=Config.SOCKET_IO_PATH)

    app.mount(Config.SOCKET_IO_MOUNT, v1_socket_io_app)

    logger.info('start socket.io service')
    logger.info('start socket.io version 5')

    return app
