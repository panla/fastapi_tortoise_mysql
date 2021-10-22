from fastapi import APIRouter

from extensions import Route, error_response, resp_success
from sockets import socket_io
from apps.api_test.entities import SocketIOParser

router = APIRouter(route_class=Route, responses=error_response)


@router.post('/sockets')
async def sockets_response(parser: SocketIOParser):
    """测试建立socket.io连接后，是否能够主动发送消息成功"""

    payload = parser.dict()

    await socket_io.emit(
        event=payload['event'],
        data=payload['data'],
        room=payload['room'],
        namespace=payload['namespace']
        )

    return resp_success(data=None)
