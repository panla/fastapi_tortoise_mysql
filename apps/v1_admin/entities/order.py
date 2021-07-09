__all__ = [
    'ListOrderSchema', 'filter_order_dependency',
]

from typing import Optional
from typing import List

from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field


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


class ReadOrderSchema(BaseModel):
    """订单详情返回参数"""

    status_code: int = 10000
    message: str = ''
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
    """订单列表返回参数"""

    total: int = 0
    orders: Optional[List[ListOrderBaseField]]


class ListOrderSchema(BaseModel):
    status_code: int = 10000
    message: str = ''
    data: Optional[ListOrderField]


def filter_order_dependency(
        page: Optional[int] = Query(default=1, description='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40)
):
    data = {
        'page': page,
        'pagesize': pagesize
    }
    return data
