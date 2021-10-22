import socketio
from socketio import AsyncServer
from fastapi import FastAPI

from config import Config, SOCKET_IO_NAMESPACES
from extensions import logger
from .namespace import NameSpaceSIO


class SocketIO():
    def __init__(self, sio_server: AsyncServer) -> None:
        self.sio_server = sio_server

    def register_namesapce(self, ns: NameSpaceSIO):
        self.ns = ns
        self.sio_server.register_namespace(ns)

    async def emit(self, event, data, room, namespace=None, callback=None):
        await self.ns.emit(event=event, data=data, room=room, namespace=namespace, callback=callback)


sio_server = AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_io = SocketIO(sio_server)


def init_sub_app(app: FastAPI):
    """mount sub app"""

    if Config.SOCKET_IO_ON:

        socket_io_app = socketio.ASGIApp(sio_server, socketio_path=Config.SOCKET_IO_PATH)

        # register more namespaces
        for namespace in SOCKET_IO_NAMESPACES:
            ns_sio = NameSpaceSIO(namespace=namespace)
            socket_io.register_namesapce(ns_sio)

        app.mount(Config.SOCKET_IO_MOUNT, socket_io_app)

        logger.info('start socket.io service 5')

    return app
