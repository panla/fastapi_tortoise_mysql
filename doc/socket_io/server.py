import socketio
from fastapi import FastAPI

api_app = FastAPI()


class NameSpaceSIO(socketio.AsyncNamespace):

    def __init__(self, namespace=None, sio_server: socketio.AsyncServer = None):
        super(NameSpaceSIO, self).__init__(namespace)
        self.server = sio_server

    async def on_connect(self, sid, environ, auth):
        """
        该sid参数是Socket.IO会话ID，每个客户端的连接的唯一标识符。给定客户端发送的所有事件都将具有相同的 sid值
        """
        print('on connect')
        print(self.namespace)
        await self.emit(event='my_response', data={'data': 'connect -> my_response'})

    async def on_disconnect(self, sid):
        """
        断开连接
        """

        await self.disconnect(sid=sid)

    async def on_join_room(self, sid, data):
        """
        加入room
        """

        print(data)
        print('加入房间')
        self.enter_room(sid=sid, room='1')
        await self.emit(event='my_response', data=data + 1, room='1')
        print('已加入房间')

    def on_leave_room(self, sid, data):
        """
        离开room
        """

        room = data.get('room')
        self.leave_room(sid=sid, room=room)

    async def on_my_event(self, sid, data):
        print('向 my_response 发送数据')
        print(data)
        room = '1'
        await self.emit(event='my_response', data=data + 1, room=room)
        print('已向 my_response 发送数据')


sio_server = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
n_sio = NameSpaceSIO('/chat', sio_server=sio_server)

sio_server.register_namespace(n_sio)

app = socketio.ASGIApp(sio_server, socketio_path='socket.io')

api_app.mount('/ws', app)
