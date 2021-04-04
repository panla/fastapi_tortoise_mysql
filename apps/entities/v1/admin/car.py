from typing import Optional
from typing import List

from fastapi import Body
from pydantic import BaseModel
from pydantic.fields import Field


class CarBaseField(BaseModel):
    id: int = Field(..., title='汽车id')
    brand: str = Field(..., title='品牌')
    price: int = Field(..., title='价格')
    is_delete: bool = Field(..., title='删除标识')

    class Config:
        orm_mode = True


class CarIdField(BaseModel):
    id: int

    class Config:
        orm_mode = True


class ListCarBaseField(BaseModel):
    total: int = 0
    cars: Optional[List[CarBaseField]]


class ReadCarSchema(BaseModel):
    """汽车详情参数"""

    code: int = 10000
    message: str = ''
    data: Optional[CarBaseField]


class ListCarSchema(BaseModel):
    """汽车列表参数"""

    code: int = 10000
    message: str = ''
    data: Optional[ListCarBaseField]


class CarSchema(BaseModel):
    """创建，删除，更新 汽车后返回的参数"""

    code: int = 10000
    message: str = ''
    data: Optional[CarIdField]


class CreateCarParameter(BaseModel):
    """创建汽车所需参数"""

    brand: str = Body(..., title='品牌', max_length=100, min_length=1)
    price: int = Body(..., title='品牌', ge=1)


class UpdateCarParameter(BaseModel):
    """更新汽车所需参数"""

    brand: Optional[str] = Body(None, title='品牌', max_length=100, min_length=1)
    price: Optional[int] = Body(None, title='品牌', ge=1)
