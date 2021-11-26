import argparse

import socketio

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=False, default='http://127.0.0.1:8000', type=str, help='service address')
parser.add_argument('-n', '--namespace', required=False, default='/chat', type=str, help='namespace')
parser.add_argument('-p', '--path', required=False, default='socket.io', type=str, help='socket.io.path')

params = parser.parse_args().__dict__

url = params.get('url')
namespace = params.get('namespace')
namespaces = [namespace]
socket_io_path = params.get('path')

sio = socketio.Client()

sio.connect(url, namespaces=namespaces, socketio_path=socket_io_path)


def main():

    sio.emit('join_room', data={'room': 1, 'user_phone': '13911111111'}, namespace=namespace)
    print('加入房间')

    sio.emit('leave_room', data={'room': 1, 'user_phone': '13911111111'}, namespace=namespace)
    print('离开房间')


main()

sio.disconnect()
