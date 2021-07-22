__all__ = [
    'ReadQuestionSchema', 'ListQuestionSchema', 'FilterQuestionParser',
]

from typing import Optional
from typing import List

from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field


class OwnerField(BaseModel):
    id: int = Field(..., title='提问者id')
    cellphone: str = Field(..., title='提问者手机号')
    name: str = Field(default='', title='提问者用户名')

    class Config:
        orm_mode = True


class ReadQuestionField(BaseModel):
    id: int = Field(..., title='问题id')
    title: str = Field(..., title='问题')
    content: str = Field(..., title='问题内容')
    created_time: str = Field(..., title='创建时间')
    updated_time: str = Field(..., title='更新时间')
    owner: Optional[OwnerField]

    class Config:
        orm_mode = True


class ReadQuestionSchema(BaseModel):
    """the response schema of one question`detail info"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ReadQuestionField]


class ListQuestionBaseField(BaseModel):
    id: int = Field(..., title='问题id')
    title: str = Field(..., title='问题')
    content: str = Field(..., title='问题内容')
    created_time: str = Field(..., title='创建时间')
    owner: Optional[OwnerField]

    class Config:
        orm_mode = True


class ListQuestionField(BaseModel):
    total: int = 0
    questions: Optional[List[ListQuestionBaseField]]


class ListQuestionSchema(BaseModel):
    """the response schema of questions`info"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ListQuestionField]


class FilterQuestionParser(BaseModel):
    """the params of filter questions"""

    page: Optional[int] = Query(default=1, description='页数', gte=1),
    pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40)
