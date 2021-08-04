__all__ = [
    'ListOrderSchema', 'FilterOrderParser',
]

from typing import Optional
from typing import List

from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field

from apps.mixins import SchemaMixin, FilterParserMixin


class OwnerField(BaseModel):
    id: int = Field(..., title='提问者id')
    cellphone: str = Field(..., title='提问者手机号')
    name: str = Field(..., title='提问者用户名')

    class Config:
        orm_mode = True


class ReadOrderField(BaseModel):
    id: int = Field(..., title='问题id')
    amount: int = Field(..., title='订单总额')
    remarks: str = Field(..., title='备注')
    created_time: str = Field(..., title='创建时间')
    updated_time: str = Field(..., title='更新时间')
    owner: OwnerField

    class Config:
        orm_mode = True


class ReadOrderSchema(SchemaMixin):
    """the response schema of one order`detail info"""

    data: Optional[ReadOrderField]


class ListOrderBaseField(BaseModel):
    id: int = Field(..., title='问题id')
    amount: int = Field(..., title='订单总额')
    remarks: str = Field(..., title='备注')
    created_time: str = Field(..., title='创建时间')
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
