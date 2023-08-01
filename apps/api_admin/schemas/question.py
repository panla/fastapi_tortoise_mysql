__all__ = [
    'ReadQuestionSchema',
    'ListQuestionSchema',
    'FilterQuestionParser'
]

from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field

from extensions import SchemaMixin, FilterParserMixin


class OwnerEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title='the question`s owner`s id')
    cellphone: str = Field(..., title='the question`s owner`s cellphone')
    name: str = Field(default='', title='the question`s owner`s name')


class QuestionEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title='the id of question')
    title: str = Field(..., title='title of question')
    content: str = Field(..., title='content of question')
    created_time: str = Field(..., title='create datetime of question')
    owner: Optional[OwnerEntity]


class ReadQuestionSchema(SchemaMixin):
    """the response schema of one question`detail info"""

    class QuestionEntity(QuestionEntity):
        model_config = ConfigDict(from_attributes=True)

        updated_time: str = Field(..., title='update datetime of question')

    data: QuestionEntity


class ListQuestionSchema(SchemaMixin):
    """the response schema of questions`info"""

    class ListQuestionEntity(BaseModel):
        total: Optional[int] = Field(0, title='total')
        questions: Optional[List[QuestionEntity]]

    data: ListQuestionEntity


class FilterQuestionParser(FilterParserMixin):
    """the params of filter questions"""
