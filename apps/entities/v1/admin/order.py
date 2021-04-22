from typing import Optional
from typing import List

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

    class Config:
        orm_mode = True


class ReadOrderSchema(BaseModel):
    """订单详情返回参数"""

    id: int = Field(..., title='问题id')
    amount: int = Field(..., title='订单总额')
    remarks: str = Field(..., title='备注')
    owner: OwnerBaseField

    class Config:
        orm_mode = True


class ListOrderSchema(BaseModel):
    """订单列表返回参数"""

    total: int = 0
    orders: Optional[List[OrderBaseField]]


read_order_exclude = ('owner.questions', 'owner.admin_user')
list_order_exclude = ('owner.questions', 'owner.admin_user')
