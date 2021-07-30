import socketio

sio = socketio.Client()
sio.connect('http://127.0.0.1:8000/ws/socket.io', namespaces=['/chat'])


@sio.on('connect')
def connect():
    print('I start connect')

    sio.emit('join_room', data=1, namespace='/chat')
    print('加入房间')


@sio.on('my_response', namespace='/chat')
def my_response(data):
    print(data)
    sio.emit('my_event', data=data + 1, namespace='/chat')
    print('向 my_event 发送')


connect()
