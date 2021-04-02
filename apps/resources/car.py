from fastapi import APIRouter

from apps.models.car import Car
from apps.entities.car import CarDetailField, CarListField, CarCreateField, CarDeleteField
from apps.entities.car import CarCreateBody
from apps.utils.response import resp_200, resp_201, resp_400, resp_404
from apps.extend.route import Route

router = APIRouter(route_class=Route)


@router.get('/cars/{c_id}', response_model=CarDetailField, status_code=200)
async def read_car(c_id: int):
    """汽车详情接口"""

    car = await Car.get_or_none(id=c_id)
    if car:
        return resp_200(data=car)
    return resp_404(message='该汽车不存在')


@router.get('/cars', response_model=CarListField, status_code=200)
async def list_cars():
    """汽车列表接口"""

    cars = Car.all()
    total = await cars.count()
    cars = await cars

    return resp_200(data={'total': total, 'cars': cars})


@router.post('/cars', response_model=CarCreateField, status_code=201)
async def create_car(car: CarCreateBody):
    """创建汽车接口"""

    c = await Car.create(**car.dict())
    return resp_201(data={'id': c.id})


@router.delete('/cars/{c_id}', response_model=CarDeleteField, status_code=201)
async def delete_car(c_id: int):
    """删除汽车，更新汽车is_delete"""

    car = await Car.get_or_none(id=c_id)
    if car:
        car.is_delete = False
        await car.save()
        return resp_201(data=car)
    return resp_404(message='该汽车不存在')
