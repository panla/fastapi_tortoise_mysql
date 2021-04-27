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
    """创建，更新，删除用户返回的字段"""
    id: int = Field(..., title='id')

    class Config:
        orm_model = True


class ReadUserSchema(BaseModel):
    """用户详情返回的字段"""

    id: int = Field(..., title='id')
    cellphone: str = Field(..., title='手机号')
    name: str = Field(..., title='账户名')
    is_delete: bool = Field(..., title='删除标识')
    is_admin_user: bool = Field(..., title='是否是管理员')

    class Config:
        orm_model = True


class ListUserSchema(BaseModel):
    """用户列表返回的字段"""

    total: int
    users: Optional[List[ListUserBaseField]]


class CreateUserParams(BaseModel):
    """创建用户的参数"""
    cellphone: str = Body(..., title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


class PatchUserParams(BaseModel):
    """更新用户的参数"""

    cellphone: Optional[str] = Body(None, title='手机号', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='名称', min_length=2, max_length=30)


def filter_params(
        page: Optional[int] = Query(default=1, title='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, title='每页数', gte=1, lte=40),
        cellphone: Optional[str] = Query(default=None, title='手机号', min_length=4, max_length=11)
):
    """搜索用户的依赖"""

    data = {
        'page': page,
        'pagesize': pagesize,
        'cellphone': cellphone
    }
    return data


read_exclude = ('admin_user', 'orders', 'questions')
read_include = ('id', 'cellphone', 'name', 'is_delete')
read_computed = ('is_admin_user',)
list_include = ('id', 'cellphone', 'name', 'is_delete')
list_computed = ('is_admin_user',)
