__all__ = [
    'ReadUserSchema', 'ListUserSchema', 'UserSchema', 'PatchUserParser', 'filter_user_dependency'
]

from typing import Optional
from typing import List

from fastapi import Body
from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field


class UserField(BaseModel):
    id: int = Field(..., title='id')

    class Config:
        orm_model = True


class UserSchema(BaseModel):
    """the response schema of create/update/delete one user"""

    status_code: int = 10000
    message: str = ''
    data: Optional[UserField]


class ReadUserField(BaseModel):
    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class ReadUserSchema(BaseModel):
    """the response schema of one user`detail info"""

    status_code: int = 10000
    message: str = ''
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


class ListUserSchema(BaseModel):
    """the response schema of user`info"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ListUserField]


class CreateUserParser(BaseModel):
    """the params of create one user"""
    cellphone: str = Body(..., title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


class PatchUserParser(BaseModel):
    """the params of update one user"""

    cellphone: Optional[str] = Body(None, title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


def filter_user_dependency(
        page: Optional[int] = Query(default=1, description='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40),
        cellphone: Optional[str] = Query(default=None, description='手机号', min_length=4, max_length=11)
):
    """the params of search user"""

    data = {
        'page': page,
        'pagesize': pagesize,
        'cellphone': cellphone
    }
    return data
