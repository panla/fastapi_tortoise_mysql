__all__ = [
    'CreateTokenParser', 'TokenSchema',
]

from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class CreateTokenParser(BaseModel):
    cellphone: str = Field(..., title='手机号', min_length=11, max_length=11)
    code: str = Field(..., title='短信验证码', min_length=4, max_length=8)


class TokenField(BaseModel):
    token: str = Field(..., title='生成token')
    user_id: int = Field(..., title='用户id')
    admin_user_id: int = Field(..., title='管理员id')


class TokenSchema(BaseModel):
    status_code: int = 10000
    message: str = ''
    data: Optional[TokenField]
