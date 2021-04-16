from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class CreateTokenParameter(BaseModel):
    cellphone: str = Field(..., description='手机号', min_length=11, max_length=11)
    code: str = Field(..., description='短信验证码', min_length=4, max_length=8)


class TokenBaseField(BaseModel):
    token: str = Field(..., description='生成token')
    user_id: int = Field(..., description='用户id')
    admin_user_id: int = Field(..., description='管理员id')


class TokenSchema(BaseModel):
    status_code: int = 10000
    message: str = ''
    data: Optional[TokenBaseField]
