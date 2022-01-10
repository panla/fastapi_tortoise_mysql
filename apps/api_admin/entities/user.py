__all__ = [
    'ReadUserSchema',
    'ListUserSchema',
    'UserSchema',
    'PatchUserParser',
    'FilterUserParser'
]

from typing import Optional, List

from fastapi import Body, Query
from pydantic import BaseModel, Field

from extensions import SchemaMixin, FilterParserMixin


class UserIDEntity(BaseModel):
    id: int = Field(..., title='id of user')

    class Config:
        orm_model = True


class UserSchema(SchemaMixin):
    """the response schema of create/update/delete one user"""

    data: Optional[UserIDEntity]


class UserEntity(BaseModel):
    id: int = Field(..., title='id of user')
    cellphone: str = Field(..., title='cellphone of user')
    name: str = Field(..., title='name of user')
    is_delete: bool = Field(..., title='is_delete flag of user')
    is_admin_user: bool = Field(..., title='is admin user')

    class Config:
        orm_model = True


class ReadUserSchema(SchemaMixin):
    """the response schema of one user`detail info"""

    class UserEntity(UserEntity):
        class Config:
            orm_model = True

    data: UserEntity


class ListUserSchema(SchemaMixin):
    """the response schema of user`info"""

    class ListUserEntity(BaseModel):
        total: int
        users: Optional[List[UserEntity]]

    data: ListUserEntity


class CreateUserParser(BaseModel):
    """the params of create one user"""

    cellphone: str = Body(..., title='cellphone of user', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='name of user', min_length=2, max_length=30)


class PatchUserParser(BaseModel):
    """the params of update one user"""

    cellphone: Optional[str] = Body(None, title='cellphone of user', min_length=11, max_length=11)
    name: Optional[str] = Body(None, title='name of user', min_length=2, max_length=30)


class FilterUserParser(FilterParserMixin):
    """the params of filter users"""

    cellphone: Optional[str] = Query(default=None, description='cellphone of user', min_length=4, max_length=11)
