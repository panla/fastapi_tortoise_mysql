import argparse

import socketio

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=False, default='http://127.0.0.1:8000', type=str, help='service address')
parser.add_argument('-n', '--namespace', required=True, type=str, help='namespace')
parser.add_argument('-p', '--path', required=False, default='socket.io', type=str, help='socket.io.path')

params = parser.parse_args().__dict__

url = params.get('url')
namespaces = [params.get('namespace')]
namespace = params.get('namespace')
socket_io_path = params.get('path')

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
