__all__ = [
    'ListOrderSchema', 'FilterOrderParser',
]

from typing import Optional
from typing import List

from pydantic import BaseModel
from pydantic.fields import Field

from apps.mixins import SchemaMixin, FilterParserMixin


class OwnerField(BaseModel):
    id: int = Field(..., title='the order`s owner`s id')
    cellphone: str = Field(..., title='the order`s owner`s cellphone')
    name: str = Field(..., title='the order`s owner`s name')

    class Config:
        orm_mode = True


class ReadOrderField(BaseModel):
    id: int = Field(..., title='id of order')
    amount: int = Field(..., title='the amount of order')
    remarks: str = Field(..., title='the remarks of order')
    created_time: str = Field(..., title='the create datetime of order')
    updated_time: str = Field(..., title='the update datetime of order')
    owner: OwnerField

    class Config:
        orm_mode = True


class ReadOrderSchema(SchemaMixin):
    """the response schema of one order`detail info"""

    data: Optional[ReadOrderField]


class ListOrderBaseField(BaseModel):
    id: int = Field(..., title='id of order')
    amount: int = Field(..., title='the amount of order')
    remarks: str = Field(..., title='the remarks of order')
    created_time: str = Field(..., title='the create datetime of order')
    owner: OwnerField

    class Config:
        orm_mode = True


class ListOrderField(BaseModel):

    total: int = 0
    orders: Optional[List[ListOrderBaseField]]


class ListOrderSchema(SchemaMixin):
    """the response schema of orders`info"""

    data: Optional[ListOrderField]


class FilterOrderParser(FilterParserMixin):
    """the params of filter orders"""
