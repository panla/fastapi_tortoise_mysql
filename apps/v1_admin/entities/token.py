from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class CreateTokenParameter(BaseModel):
    cellphone: str = Field(..., title='手机号', min_length=11, max_length=11)
    code: str = Field(..., title='短信验证码', min_length=4, max_length=8)


class TokenSchema(BaseModel):
    token: str = Field(..., title='生成token')
    user_id: int = Field(..., title='用户id')
    admin_user_id: int = Field(..., title='管理员id')