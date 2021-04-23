from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field


class OwnerBaseField(BaseModel):
    id: int = Field(..., title='提问者id')
    cellphone: str = Field(..., title='提问者手机号')
    name: str = Field(default='', title='提问者用户名')

    class Config:
        orm_mode = True


class QuestionBaseField(BaseModel):
    id: int = Field(..., title='问题id')
    title: str = Field(..., title='问题')
    content: str = Field(..., title='问题内容')
    owner: Optional[OwnerBaseField]
    created_time: str = Field(..., description='创建时间')

    class Config:
        orm_mode = True


class ReadQuestionSchema(BaseModel):
    """问题详情返回参数"""

    id: int = Field(..., title='问题id')
    title: str = Field(..., title='问题')
    content: str = Field(..., title='问题内容')
    owner: Optional[OwnerBaseField]
    created_time: str = Field(..., description='创建时间')
    updated_time: str = Field(..., description='更新时间')

    class Config:
        orm_mode = True


class ListQuestionSchema(BaseModel):
    """问题列表返回参数"""

    total: int = 0
    questions: Optional[List[QuestionBaseField]]


read_exclude = ('owner.orders', 'owner.admin_user')
read_computed = ('created_time', 'updated_time')
list_exclude = ('owner.orders', 'owner.admin_user')
list_computed = ('created_time',)
