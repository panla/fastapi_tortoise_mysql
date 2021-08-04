__all__ = [
    'ReadQuestionSchema', 'ListQuestionSchema', 'FilterQuestionParser',
]

from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field

from apps.mixins import SchemaMixin, FilterParserMixin


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


class ReadQuestionSchema(SchemaMixin):
    """the response schema of one question`detail info"""

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


class ListQuestionSchema(SchemaMixin):
    """the response schema of questions`info"""

    data: Optional[ListQuestionField]


class FilterQuestionParser(FilterParserMixin):
    """the params of filter questions"""
