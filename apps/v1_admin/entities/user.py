__all__ = [
    'ReadUserSchema', 'ListUserSchema', 'UserSchema', 'PatchUserParser', 'FilterUserParser',
]

from typing import Optional
from typing import List

from fastapi import Body
from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field

from apps.mixins import SchemaMixin, FilterParserMixin


class UserField(BaseModel):
    id: int = Field(..., title='id')

    class Config:
        orm_model = True


class UserSchema(SchemaMixin):
    """the response schema of create/update/delete one user"""

    data: Optional[UserField]


class ReadUserField(BaseModel):
    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class ReadUserSchema(SchemaMixin):
    """the response schema of one user`detail info"""

    data: Optional[ReadUserField]


class ListUserBaseField(BaseModel):
    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class ListUserField(BaseModel):
    total: int
    users: Optional[List[ListUserBaseField]]


class ListUserSchema(SchemaMixin):
    """the response schema of user`info"""

    data: Optional[ListUserField]


class CreateUserParser(BaseModel):
    """the params of create one user"""
    cellphone: str = Body(..., title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


class PatchUserParser(BaseModel):
    """the params of update one user"""

    cellphone: Optional[str] = Body(None, title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


class FilterUserParser(FilterParserMixin):
    """the params of filter users"""

    cellphone: Optional[str] = Query(default=None, description='手机号', min_length=4, max_length=11)
