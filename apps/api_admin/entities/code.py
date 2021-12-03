__all__ = [
    'CreateCodeParser',
    'CreateCodeSchema'
]

from fastapi import Body
from pydantic import BaseModel
from pydantic.fields import Field

from mixins import SchemaMixin


class CreateCodeField(BaseModel):
    code: str = Field(..., title='sms code', min_length=4, max_length=8)
    success: bool = Field(True, title='success')


class CreateCodeSchema(SchemaMixin):
    """the response schema of create sms code"""

    data: CreateCodeField


class CreateCodeParser(BaseModel):
    """the parama of create sms code"""

    cellphone: str = Body(..., title='cellphone', min_length=11, max_length=14)
