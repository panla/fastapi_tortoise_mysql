import socketio
from fastapi import FastAPI


sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
v1_socket_io_app = socketio.ASGIApp(sio, socketio_path='socket.io')


class NameSpaceSIO(socketio.AsyncNamespace):

    def __init__(self, sio: socketio.AsyncServer):
        super().__init__(sio)
        self.sio = sio

    async def on_connect(self, sid, environ, auth):
        """
        该sid参数是Socket.IO会话ID，每个客户端的连接的唯一标识符。给定客户端发送的所有事件都将具有相同的 sid值
        """

        pass

    async def on_disconnect(self, sid):
        """
        断开连接
        """

        await self.sio.disconnect(sid=sid, namespace=self.namespace)

    def on_join_room(self, sid, data):
        """
        加入room
        """

        room = data.get('room')
        self.sio.enter_room(sid=sid, room=room, namespace=self.namespace)

    def on_leave_room(self, sid, data):
        """
        离开room
        """
        
        room = data.get('room')
        self.sio.leave_room(sid=sid, room=room, namespace=self.namespace)


    async def on_my_event(self, sid, data):
        room = data.get('room')
        await self.emit(event='my_response', data={'data': 'on_my_event -> on_my_response'}, room=room)


n_sio = NameSpaceSIO(namespace='/chat', sio=sio)


def init_sub_app(app: FastAPI):
    """注册子app"""

    app.mount(path='/api/v1', app=v1_socket_io_app, name='v1_socket_io')
