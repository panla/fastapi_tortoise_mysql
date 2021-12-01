from fastapi import Body
from pydantic import BaseModel


class SocketIODataParser(BaseModel):
    msg: str = Body(..., title='message')


class SocketIOParser(BaseModel):
    event: str = Body(..., title='socket.io event')
    namespace: str = Body(..., title='socket.io namespace')
    room: str = Body(..., title='socket.io room')
    data: SocketIODataParser
