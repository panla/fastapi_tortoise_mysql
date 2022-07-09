__all__ = [
    'ListOrderSchema',
    'ReadOrderSchema',
    'FilterOrderParser'
]

from typing import Optional, List

from pydantic import BaseModel, Field

from extensions import SchemaMixin, FilterParserMixin


class OwnerEntity(BaseModel):
    id: int = Field(..., title='the order`s owner`s id')
    cellphone: str = Field(..., title='the order`s owner`s cellphone')
    name: str = Field(..., title='the order`s owner`s name')

    class Config:
        orm_mode = True


class OrderEntity(BaseModel):
    id: int = Field(..., title='id of order')
    amount: int = Field(..., title='the amount of order')
    remarks: str = Field(..., title='the remarks of order')
    created_time: str = Field(..., title='the create datetime of order')
    owner: OwnerEntity

    class Config:
        orm_mode = True


class ReadOrderSchema(SchemaMixin):
    """the response schema of one order`detail info"""

    class OrderEntity(OrderEntity):
        updated_time: str = Field(..., title='the update datetime of order')

        class Config:
            orm_mode = True

    data: OrderEntity


class ListOrderSchema(SchemaMixin):
    """the response schema of orders`info"""

    class ListOrderEntity(BaseModel):
        total: Optional[int] = Field(0, title='total')
        orders: Optional[List[OrderEntity]]

    data: ListOrderEntity


class FilterOrderParser(FilterParserMixin):
    """the params of filter orders"""
