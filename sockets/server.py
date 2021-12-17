import socketio
from socketio import AsyncServer
from fastapi import FastAPI

from config import SocketIOConfig, ServiceConfig
from extensions import logger
from .namespace import NameSpaceSIO


class SocketIO():
    def __init__(self, sio_server: AsyncServer) -> None:
        self.sio_server = sio_server

    def register_namespace(self, ns: NameSpaceSIO):
        self.ns = ns
        self.sio_server.register_namespace(ns)

    async def emit(self, event, data, room, namespace=None, callback=None):
        await self.ns.emit(event=event, data=data, room=room, namespace=namespace, callback=callback)


sio_server = AsyncServer(async_mode='asgi', cors_allowed_origins='*')
socket_io = SocketIO(sio_server)


def init_sub_app(app: FastAPI):
    """mount sub app"""

    if ServiceConfig.SOCKET_IO_ON:

        socket_io_app = socketio.ASGIApp(sio_server, socketio_path=SocketIOConfig.SOCKET_IO_PATH)

        # register more namespaces
        for namespace in SocketIOConfig.SOCKET_IO_NAMESPACES:
            ns_sio = NameSpaceSIO(namespace=namespace)
            socket_io.register_namespace(ns_sio)

        app.mount(SocketIOConfig.SOCKET_IO_MOUNT, socket_io_app)

        logger.info('start socket.io service 5')

    return app
