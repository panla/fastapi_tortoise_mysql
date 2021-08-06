import socketio
from fastapi import FastAPI

from event import NameSpaceSIO

namespace = '/chat'
socket_io_path = 'socket.io'

app = FastAPI()


def main():
    ns_sio = NameSpaceSIO(namespace)

    sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

    sio_server.register_namespace(ns_sio)

    sio_app = socketio.ASGIApp(sio_server, other_asgi_app=app, socketio_path=socket_io_path)

    return sio_app


sio_app = main()
