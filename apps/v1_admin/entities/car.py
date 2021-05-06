from typing import Optional
from typing import List

from fastapi import Body, Query
from pydantic import BaseModel
from pydantic.fields import Field


class ReadCarField(BaseModel):
    id: int = Field(..., title='汽车id')
    brand: str = Field(..., title='品牌')
    price: int = Field(..., title='价格')
    is_delete: bool = Field(..., title='删除标识')

    class Config:
        orm_mode = True


class ReadCarSchema(BaseModel):
    """汽车详情参数"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ReadCarField]


class ListCarBaseField(BaseModel):
    id: int = Field(..., title='汽车id')
    brand: str = Field(..., title='品牌')
    price: int = Field(..., title='价格')
    is_delete: bool = Field(..., title='删除标识')

    class Config:
        orm_mode = True


class ListCarField(BaseModel):
    total: int = 0
    cars: Optional[List[ListCarBaseField]]


class ListCarSchema(BaseModel):
    """汽车列表参数"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ListCarField]


class CarField(BaseModel):
    id: int

    class Config:
        orm_mode = True


class CarSchema(BaseModel):
    """创建，删除，更新 汽车后返回的参数"""

    status_code: int = 10000
    message: str = ''
    data: Optional[CarField]


class CreateCarParameter(BaseModel):
    """创建汽车所需参数"""

    brand: str = Body(..., title='品牌', max_length=100, min_length=1)
    price: int = Body(..., title='品牌', ge=1)


class PatchCarParameter(BaseModel):
    """更新汽车所需参数"""

    brand: Optional[str] = Body(None, title='品牌', max_length=100, min_length=1)
    price: Optional[int] = Body(None, title='品牌', ge=1)


def filter_params(
        page: Optional[int] = Query(default=1, title='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, title='每页数', gte=1, lte=40),
        brand: Optional[str] = Query(default=None, title='品牌', max_length=50)
):
    data = {
        'page': page,
        'pagesize': pagesize,
        'brand': brand
    }
    return data
