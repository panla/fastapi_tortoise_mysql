__all__ = [
    'ReadCarSchema',
    'ListCarSchema',
    'CarIDSchema',
    'CreateCarParser',
    'PatchCarParser',
    'FilterCarParser'
]

from typing import Optional, List

from fastapi import Body, Query
from pydantic import BaseModel, ConfigDict, Field

from extensions import SchemaMixin, FilterParserMixin


class CarEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int = Field(..., title='id of car')
    brand: str = Field(..., title='brand of car')
    price: int = Field(..., title='price of car', description='the unit is cent')
    is_delete: bool = Field(..., title='is_delete flag of car')


# read car
class ReadCarSchema(SchemaMixin):
    """the response schema of one car`detail info"""

    data: CarEntity


# list car
class ListCarSchema(SchemaMixin):
    """the response schema of cars`info"""

    class ListCarEntity(BaseModel):
        total: Optional[int] = Field(0, title='total')
        cars: Optional[List[CarEntity]]

    data: ListCarEntity


# create update car schema
class CarIDSchema(SchemaMixin):
    """the response schema of create/delete/update one car"""

    class CarIDEntity(BaseModel):
        model_config = ConfigDict(from_attributes=True)

        id: int = Field(..., title='car.id')

    data: CarIDEntity


# create update
class CreateCarParser(BaseModel):
    """the params of create one car"""

    brand: str = Body(..., title='brand of car', max_length=100, min_length=1)
    price: int = Body(..., title='price of car', ge=1)


class PatchCarParser(BaseModel):
    """the params of update one car"""

    brand: Optional[str] = Body(None, title='brand of car', max_length=100, min_length=1)
    price: Optional[int] = Body(None, title='price of car', ge=1)


# list filter car
class FilterCarParser(FilterParserMixin):
    """the params of filter cars"""

    brand: Optional[str] = Query(default=None, description='brand of car', max_length=50)
