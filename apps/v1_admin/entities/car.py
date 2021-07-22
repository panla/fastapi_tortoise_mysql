__all__ = [
    'ReadCarSchema', 'ListCarSchema', 'CarSchema', 'CreateCarParser', 'PatchCarParser', 'filter_car_dependency',
]

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
    """the response schema of one car`detail info"""

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
    """the response schema of cars`info"""

    status_code: int = 10000
    message: str = ''
    data: Optional[ListCarField]


class CarField(BaseModel):
    id: int

    class Config:
        orm_mode = True


class CarSchema(BaseModel):
    """the response schema of create/delete/update one car"""

    status_code: int = 10000
    message: str = ''
    data: Optional[CarField]


class CreateCarParser(BaseModel):
    """the params of create one car"""

    brand: str = Body(..., title='品牌', max_length=100, min_length=1)
    price: int = Body(..., title='价格', ge=1)


class PatchCarParser(BaseModel):
    """the params of update one car"""

    brand: Optional[str] = Body(None, title='品牌', max_length=100, min_length=1)
    price: Optional[int] = Body(None, title='价格', ge=1)


def filter_car_dependency(
        page: Optional[int] = Query(default=1, description='页数', gte=1),
        pagesize: Optional[int] = Query(default=None, description='每页数', gte=1, lte=40),
        brand: Optional[str] = Query(default=None, description='品牌', max_length=50)
):
    data = {
        'page': page,
        'pagesize': pagesize,
        'brand': brand
    }
    return data
