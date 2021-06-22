import socketio
from fastapi import FastAPI


class NameSpaceSIO(socketio.AsyncNamespace):

    def __init__(self, namespace=None, sio_server: socketio.AsyncServer = None):
        super(NameSpaceSIO, self).__init__(namespace)
        self.server = sio_server

    async def on_connect(self, sid, environ, auth):
        """
        该sid参数是Socket.IO会话ID，每个客户端的连接的唯一标识符。给定客户端发送的所有事件都将具有相同的 sid值
        """

        pass

    async def on_disconnect(self, sid):
        """
        断开连接
        """

        await self.disconnect(sid=sid)

    def on_join_room(self, sid, data):
        """
        加入room
        """

        room = data.get('room')
        self.enter_room(sid=sid, room=room)

    def on_leave_room(self, sid, data):
        """
        离开room
        """

        room = data.get('room')
        self.leave_room(sid=sid, room=room)

    async def on_my_event(self, sid, data):
        room = data.get('room')
        send_data = {'data': 'on_my_event -> on_my_response'}
        await self.emit(event='my_response', data=data, room=room)


sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
n_sio = NameSpaceSIO(namespace='/chat', sio_server=sio_server)

sio_server.register_namespace(n_sio)

v1_socket_io_app = socketio.ASGIApp(sio_server, socketio_path='socket.io')


def init_sub_app(app: FastAPI):
    """注册子app"""

    app.mount(path='/api/v1', app=v1_socket_io_app, name='v1_socket_io')
    app.n_sio = n_sio
    app.sio_server = sio_server


__all__ = ['n_sio', 'sio_server', 'init_sub_app']
