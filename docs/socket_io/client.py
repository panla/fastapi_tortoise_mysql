import argparse

import socketio

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', required=False, default='http://127.0.0.1:8000', type=str, help='service address')
parser.add_argument('-n', '--namespace', required=False, default='/chat', type=str, help='namespace')

params = parser.parse_args().__dict__

url = params.get('url')
namespace = params.get('namespace')
namespaces = [namespace]
socket_io_path = params.get('path')

sio = socketio.Client()

sio.connect(url, namespaces=namespaces)


def main():

    sio.emit('join_room', data={'room': 1, 'user_phone': '13911111111'}, namespace=namespace)
    print('enter room')

    sio.emit('leave_room', data={'room': 1, 'user_phone': '13911111111'}, namespace=namespace)
    print('leave room')


main()

sio.disconnect()
