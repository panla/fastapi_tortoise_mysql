from typing import Optional
from typing import List

from fastapi import Query
from pydantic import BaseModel
from pydantic.fields import Field


class OwnerBaseField(BaseModel):
    id: int = Field(..., title='提问者id')
    cellphone: str = Field(..., title='提问者手机号')
    name: str = Field(..., title='提问者用户名')

    class Config:
        orm_mode = True


class OrderBaseField(BaseModel):
    id: int = Field(..., title='问题id')
    amount: int = Field(..., title='订单总额')
    remarks: str = Field(..., title='备注')
    owner: OwnerBaseField
    created_time: str = Field(..., title='创建时间')

    class Config:
        orm_mode = True


class ReadOrderSchema(BaseModel):
    """订单详情返回参数"""

    id: int = Field(..., title='问题id')
    amount: int = Field(..., title='订单总额')
    remarks: str = Field(..., title='备注')
    owner: OwnerBaseField
    created_time: str = Field(..., title='创建时间')
    updated_time: str = Field(..., title='更新时间')

    class Config:
        orm_mode = True


class ListOrderSchema(BaseModel):
    """订单列表返回参数"""

    total: int = 0
    orders: Optional[List[OrderBaseField]]


def filter_params(
        page: Optional[int] = Query(default=1, description='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40)
):
    data = {
        'page': page,
        'pagesize': pagesize
    }
    return data


read_exclude = ('owner.questions', 'owner.admin_user')
read_computed = ('created_time', 'updated_time')
list_order_exclude = ('owner.questions', 'owner.admin_user')
list_computed = ('created_time',)
