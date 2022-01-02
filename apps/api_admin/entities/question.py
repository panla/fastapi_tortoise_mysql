__all__ = [
    'ReadQuestionSchema',
    'ListQuestionSchema',
    'FilterQuestionParser'
]

from typing import Optional, List

from pydantic import BaseModel, Field

from mixins import SchemaMixin, FilterParserMixin


class OwnerEntity(BaseModel):
    id: int = Field(..., title='the question`s owner`s id')
    cellphone: str = Field(..., title='the question`s owner`s cellphone')
    name: str = Field(default='', title='the question`s owner`s name')

    class Config:
        orm_mode = True


class QuestionBaseEntity(BaseModel):
    id: int = Field(..., title='the id of question')
    title: str = Field(..., title='title of question')
    content: str = Field(..., title='content of question')
    created_time: str = Field(..., title='create datetime of question')
    owner: Optional[OwnerEntity]

    class Config:
        orm_mode = True


class ReadQuestionSchema(SchemaMixin):
    """the response schema of one question`detail info"""

    class QuestionEntity(QuestionBaseEntity):
        updated_time: str = Field(..., title='update datetime of question')

        class Config:
            orm_mode = True

    data: QuestionEntity


class ListQuestionSchema(SchemaMixin):
    """the response schema of questions`info"""

    class ListQuestionEntity(BaseModel):
        total: int = 0
        questions: Optional[List[QuestionBaseEntity]]

    data: ListQuestionEntity


class FilterQuestionParser(FilterParserMixin):
    """the params of filter questions"""
