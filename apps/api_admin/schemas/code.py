__all__ = [
    'CreateCodeParser',
    'CreateCodeSchema'
]

from fastapi import Body
from pydantic import BaseModel, Field

from extensions import SchemaMixin


class CreateCodeSchema(SchemaMixin):
    """the response schema of create sms code"""

    class CreateCodeEntity(BaseModel):
        code: str = Field(..., title='sms code', min_length=4, max_length=8)
        success: bool = Field(True, title='success')

    data: CreateCodeEntity


class CreateCodeParser(BaseModel):
    """the params of create sms code"""

    cellphone: str = Body(..., title='cellphone', min_length=11, max_length=14)
