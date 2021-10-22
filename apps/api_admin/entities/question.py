__all__ = [
    'ReadQuestionSchema', 'ListQuestionSchema', 'FilterQuestionParser',
]

from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field

from mixins import SchemaMixin, FilterParserMixin


class OwnerField(BaseModel):
    id: int = Field(..., title='the question`s owner`s id')
    cellphone: str = Field(..., title='the question`s owner`s cellphone')
    name: str = Field(default='', title='the question`s owner`s name')

    class Config:
        orm_mode = True


class ReadQuestionField(BaseModel):
    id: int = Field(..., title='the id of question')
    title: str = Field(..., title='title of question')
    content: str = Field(..., title='content of question')
    created_time: str = Field(..., title='create datetime of question')
    updated_time: str = Field(..., title='update datetime of question')
    owner: Optional[OwnerField]

    class Config:
        orm_mode = True


class ReadQuestionSchema(SchemaMixin):
    """the response schema of one question`detail info"""

    data: Optional[ReadQuestionField]


class ListQuestionBaseField(BaseModel):
    id: int = Field(..., title='the id of question')
    title: str = Field(..., title='title of question')
    content: str = Field(..., title='content of question')
    created_time: str = Field(..., title='create datetime of question')
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
