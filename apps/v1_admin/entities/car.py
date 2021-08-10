__all__ = [
    'ReadCarSchema', 'ListCarSchema', 'CarSchema', 'CreateCarParser', 'PatchCarParser', 'FilterCarParser',
]

from typing import Optional
from typing import List

from fastapi import Body, Query
from pydantic import BaseModel
from pydantic.fields import Field

from mixins import SchemaMixin, FilterParserMixin


class ReadCarField(BaseModel):
    id: int = Field(..., title='id of car')
    brand: str = Field(..., title='brand of car')
    price: int = Field(..., title='price of car', description='the unit is cent')
    is_delete: bool = Field(..., title='is_delete flag of car')

    class Config:
        orm_mode = True


class ReadCarSchema(SchemaMixin):
    """the response schema of one car`detail info"""

    data: Optional[ReadCarField]


class ListCarBaseField(BaseModel):
    id: int = Field(..., title='id of car')
    brand: str = Field(..., title='brand of car')
    price: int = Field(..., title='price of car', description='the unit is cent')
    is_delete: bool = Field(..., title='is_delete flag of car')

    class Config:
        orm_mode = True


class ListCarField(BaseModel):
    total: int = 0
    cars: Optional[List[ListCarBaseField]]


class ListCarSchema(SchemaMixin):
    """the response schema of cars`info"""

    data: Optional[ListCarField]


class CarField(BaseModel):
    id: int

    class Config:
        orm_mode = True


class CarSchema(SchemaMixin):
    """the response schema of create/delete/update one car"""

    data: Optional[CarField]


class CreateCarParser(BaseModel):
    """the params of create one car"""

    brand: str = Body(..., title='brand of car', max_length=100, min_length=1)
    price: int = Body(..., title='price of car', ge=1)


class PatchCarParser(BaseModel):
    """the params of update one car"""

    brand: Optional[str] = Body(None, title='brand of car', max_length=100, min_length=1)
    price: Optional[int] = Body(None, title='price of car', ge=1)


class FilterCarParser(FilterParserMixin):
    """the params of filter cars"""

    brand: Optional[str] = Query(default=None, description='brand of car', max_length=50)
