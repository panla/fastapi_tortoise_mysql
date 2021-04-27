from typing import Optional

from fastapi import APIRouter, Query, Depends

from apps.models import AdminUser, Car
from apps.utils import raise_404, error_response
from apps.extension.route import Route
from apps.libs.admin.token import get_current_admin_user
from apps.entities.v1.admin.car import ReadCarSchema, ListCarSchema, CarSchema
from apps.entities.v1.admin.car import CreateCarParameter, PatchCarParameter
from apps.entities.v1.admin.car import filter_params

router = APIRouter(route_class=Route)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200, responses=error_response)
async def read_car(c_id: int, admin_user: AdminUser = Depends(get_current_admin_user)):
    """汽车详情接口"""

    car = await Car.get_or_none(id=c_id)
    if car:
        return car
    return raise_404(message='该汽车不存在')


@router.get('', response_model=ListCarSchema, status_code=200, responses=error_response)
async def list_cars(
        params: dict = Depends(filter_params)
):
    """汽车列表接口"""

    query = Car.all()
    total = await query.count()
    cars = await Car.paginate(query, params['page'], params['pagesize'] or total)

    return {'total': total, 'cars': cars}


@router.post('', response_model=CarSchema, status_code=201, responses=error_response)
async def create_car(car: CreateCarParameter):
    """创建汽车接口"""

    c = await Car.create(**car.dict())
    return c


@router.patch('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def update_car(c_id: int, car_item: Optional[PatchCarParameter]):
    """更新汽车"""

    car = await Car.filter(id=c_id).first()
    if car:
        await car.update_from_dict(car_item.dict())
        await car.save()
        return car
    return raise_404(message='该汽车不存在')


@router.delete('/cars/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def delete_car(c_id: int):
    """删除汽车，更新汽车删除标识"""

    car = await Car.get_or_none(id=c_id)
    if car:
        car.is_delete = False
        await car.save()
        return car
    return raise_404(message='该汽车不存在')
