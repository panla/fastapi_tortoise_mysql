import socketio

url = 'http://172.22.0.4:8000'
namespaces = ['/chat']
namespace = '/chat'
socket_io_path = 'socket.io'

sio = socketio.Client()

sio.connect(url, namespaces=namespaces, socketio_path=socket_io_path)


@sio.on('connect', namespace=namespace)
def connect():
    print('I start connect')


@sio.on('response', namespace=namespace)
def response(data):
    print(data)
    data['num'] += 1

    print('向 my_event 发送消息')
    sio.emit('my_event', data=data, namespace=namespace)


def main():
    connect()

    sio.emit('join_room', data={'num': 1, 'room': '1'}, namespace=namespace)
    print('加入房间')


main()
