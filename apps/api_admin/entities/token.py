__all__ = [
    'CreateTokenParser',
    'TokenSchema'
]

from typing import Optional

from pydantic import BaseModel
from pydantic import Field

from mixins import SchemaMixin


class CreateTokenParser(BaseModel):
    cellphone: str = Field(..., title='cellphone of user', min_length=11, max_length=11)
    code: str = Field(..., title='sms code', min_length=4, max_length=8)


class TokenField(BaseModel):
    token: str = Field(..., title='JSON Web Token string')
    user_id: int = Field(..., title='id of user')
    extend_user_id: int = Field(..., title='extend user.id')
    extend_model: str = Field(..., title='Model')


class TokenSchema(SchemaMixin):
    """the response schema of login and get token"""

    data: Optional[TokenField]
