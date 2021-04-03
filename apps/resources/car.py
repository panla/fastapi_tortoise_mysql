from typing import Optional

from fastapi import APIRouter

from apps.models.car import Car
from apps.entities.car import CarReadSchema, CarListSchema, CarSchema
from apps.entities.car import CarCreateParameter, CarUpdateParameter
from apps.utils.response import resp_200, resp_201, resp_400, resp_404
from apps.extend.route import Route

router = APIRouter(route_class=Route)


@router.get('/cars/{c_id}', response_model=CarReadSchema, status_code=200)
async def read_car(c_id: int):
    """汽车详情接口"""

    car = await Car.get_or_none(id=c_id)
    if car:
        return resp_200(data=car)
    return resp_404(message='该汽车不存在')


@router.get('/cars', response_model=CarListSchema, status_code=200)
async def list_cars():
    """汽车列表接口"""

    cars = Car.all()
    total = await cars.count()
    cars = await cars

    return resp_200(data={'total': total, 'cars': cars})


@router.post('/cars', response_model=CarSchema, status_code=201)
async def create_car(car: CarCreateParameter):
    """创建汽车接口"""

    c = await Car.create(**car.dict())
    return resp_201(data={'id': c.id})


@router.patch('/cars/{c_id}', response_model=CarSchema, status_code=201)
async def update_car(c_id: int, car_item: Optional[CarUpdateParameter]):
    """更新汽车"""

    car = await Car.filter(id=c_id).first()
    if car:
        car = await car.update_from_dict(car_item.dict())
        return resp_201(data=car)
    return resp_404(message='该汽车不存在')


@router.delete('/cars/{c_id}', response_model=CarSchema, status_code=201)
async def delete_car(c_id: int):
    """删除汽车，更新汽车删除标识"""

    car = await Car.get_or_none(id=c_id)
    if car:
        car.is_delete = False
        await car.save()
        return resp_201(data=car)
    return resp_404(message='该汽车不存在')
