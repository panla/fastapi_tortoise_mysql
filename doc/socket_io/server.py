import socketio
from fastapi import FastAPI

from manager import NameSpaceIO

namespace = '/chat'
socket_io_path = 'socket.io'

app = FastAPI()

ns_sio = NameSpaceIO(namespace)

sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio_server.register_namespace(ns_sio)

sio_app = socketio.ASGIApp(sio_server, other_asgi_app=app, socketio_path=socket_io_path)
