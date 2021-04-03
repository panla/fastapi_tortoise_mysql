from typing import Optional

from fastapi import APIRouter

from apps.models.car import Car
from apps.entities.car import ReadCarSchema, ListCarSchema, CarSchema
from apps.entities.car import CreateCarParameter, UpdateCarParameter
from apps.utils.response import resp_200, resp_201, resp_404, error_response
from apps.extend.route import Route

router = APIRouter(tags=['cars'], route_class=Route)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200, responses=error_response)
async def read_car(c_id: int):
    """汽车详情接口"""

    car = await Car.get_or_none(id=c_id)
    if car:
        return resp_200(data=car)
    return resp_404(message='该汽车不存在')


@router.get('', response_model=ListCarSchema, status_code=200, responses=error_response)
async def list_cars():
    """汽车列表接口"""

    cars = Car.all()
    total = await cars.count()
    cars = await cars

    return resp_200(data={'total': total, 'cars': cars})


@router.post('', response_model=CarSchema, status_code=201, responses=error_response)
async def create_car(car: CreateCarParameter):
    """创建汽车接口"""

    c = await Car.create(**car.dict())
    return resp_201(data={'id': c.id})


@router.patch('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def update_car(c_id: int, car_item: Optional[UpdateCarParameter]):
    """更新汽车"""

    car = await Car.filter(id=c_id).first()
    if car:
        car = await car.update_from_dict(car_item.dict())
        return resp_201(data=car)
    return resp_404(message='该汽车不存在')


@router.delete('/cars/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def delete_car(c_id: int):
    """删除汽车，更新汽车删除标识"""

    car = await Car.get_or_none(id=c_id)
    if car:
        car.is_delete = False
        await car.save()
        return resp_201(data=car)
    return resp_404(message='该汽车不存在')
