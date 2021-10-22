from typing import Optional
from typing import List

from fastapi import Body, Query
from pydantic import BaseModel
from pydantic.fields import Field

from mixins import SchemaMixin, FilterParserMixin


class SocketIODataParser(BaseModel):
    msg: str = Body(..., title='message')


class SocketIOParser(BaseModel):
    event: str = Body(..., title='socket.io event')
    namespace: str = Body(..., title='socket.io namespace')
    room: str = Body(..., title='socket.io room')
    data: SocketIODataParser
