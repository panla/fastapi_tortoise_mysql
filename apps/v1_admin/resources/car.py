from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from apps.extensions import Route, NotFound
from apps.utils import resp_success, error_response
from apps.models import AdminUser, Car
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import ReadCarSchema, ListCarSchema, CarSchema
from apps.v1_admin.entities import CreateCarParameter, PatchCarParameter
from apps.v1_admin.entities import filter_car_dependency
from apps.v1_admin.logics import filter_cars

router = APIRouter(route_class=Route)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200, responses=error_response)
async def read_car(c_id: int, admin_user: AdminUser = Depends(get_current_admin_user)):
    """汽车详情接口"""

    assert c_id > 0, f'c_id is {c_id}, it needs > 0'

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id}不存在')


@router.patch('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def patch_car(
        c_id: int,
        car_item: Optional[PatchCarParameter],
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """更新汽车"""

    assert c_id > 0, f'c_id is {c_id}, it needs > 0'

    car = await Car.filter(id=c_id, is_delete=False).first()
    if car:
        await car.update_from_dict(car_item.dict())
        await car.save()
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id}不存在')


@router.delete('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def delete_car(
        c_id: int = Path(..., description='汽车id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """删除汽车，更新汽车删除标识"""

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        car.is_delete = False
        await car.save()
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id}不存在')


@router.post('', response_model=CarSchema, status_code=201, responses=error_response)
async def create_car(car: CreateCarParameter, admin_user: AdminUser = Depends(get_current_admin_user)):
    """创建汽车接口"""

    c = await Car.create(**car.dict())
    return resp_success(data=c)


@router.get('', response_model=ListCarSchema, status_code=200, responses=error_response)
async def list_cars(
        params: dict = Depends(filter_car_dependency),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """汽车列表接口"""

    query = filter_cars(params)
    total = await query.count()
    cars = await Car.paginate(query, params['page'], params['pagesize'] or total)

    return resp_success(data={'total': total, 'cars': cars})
