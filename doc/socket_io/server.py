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

    sio_app = socketio.ASGIApp(sio_server, socketio_path=socket_io_path)

    app.mount('/', sio_app)

    return app


@app.get('/')
def index():
    return {'success': True}


app = main()
