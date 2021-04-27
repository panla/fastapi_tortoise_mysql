from typing import Optional
from typing import List

from fastapi import Body
from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field


class ListUserBaseField(BaseModel):
    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class UserSchema(BaseModel):
    id: int = Field(..., title='id')

    class Config:
        orm_model = True


class ReadUserSchema(BaseModel):
    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class ListUserSchema(BaseModel):
    total: int
    users: Optional[List[ListUserBaseField]]


class CreateUserParams(BaseModel):
    cellphone: str = Body(..., title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


class PatchUserParams(BaseModel):
    cellphone: Optional[str] = Body(None, title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


def filter_params(
        page: Optional[int] = Query(default=1, description='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40)
):
    data = {
        'page': page,
        'pagesize': pagesize
    }
    return data


read_exclude = ('admin_user', 'orders', 'questions')
read_include = ('id', 'cellphone', 'name', 'is_delete')
read_computed = ('is_admin_user',)
list_include = ('id', 'cellphone', 'name', 'is_delete')
list_computed = ('is_admin_user',)
