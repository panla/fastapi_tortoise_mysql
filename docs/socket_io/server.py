import argparse

import socketio
import uvicorn
from fastapi import FastAPI

from event import NameSpaceSIO

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--namespace', required=False, default='/chat', type=str, help='namespace')
parser.add_argument('-p', '--path', required=False, default='socket.io', type=str, help='socket.io.path')
parser.add_argument('-m', '--mount', required=False, default='/', type=str, help='app mount location')
parser.add_argument('--host', required=False, default='127.0.0.1', type=str, help='app host')
parser.add_argument('--port', required=False, default=8000, type=int, help='app port')

params = parser.parse_args()
namespace = params.namespace
socket_io_path = params.path
mount_location = params.mount
host = params.host
port = params.port

app = FastAPI()


def main():
    ns_sio = NameSpaceSIO(namespace)

    sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

    sio_server.register_namespace(ns_sio)

    sio_app = socketio.ASGIApp(sio_server, socketio_path=socket_io_path)

    app.mount(mount_location, sio_app)

    return app


@app.get('/')
def index():
    return {'success': True}


if __name__ == '__main__':
    app = main()
    uvicorn.run(app=app, host=host, port=port)
