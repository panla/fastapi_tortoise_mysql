from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from apps.extensions import Route, NotFound, error_response
from apps.utils import resp_success
from apps.models import AdminUser, Car
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import ReadCarSchema, ListCarSchema, CarSchema
from apps.v1_admin.entities import CreateCarParser, PatchCarParser, FilterCarParser
from apps.v1_admin.logics import filter_cars

router = APIRouter(route_class=Route)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200, responses=error_response)
async def read_car(c_id: int, admin_user: AdminUser = Depends(get_current_admin_user)):
    """the api of read one car"""

    assert c_id > 0, f'c_id is {c_id}, it needs > 0'

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id} not exists')


@router.patch('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def patch_car(
        c_id: int,
        parser: Optional[PatchCarParser],
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of update one car"""

    assert c_id > 0, f'c_id is {c_id}, it needs > 0'

    car = await Car.filter(id=c_id, is_delete=False).first()
    if car:
        params = dict()
        for k, v in parser.dict().items():
            if v:
                params[k] = v
        await car.update_from_dict(params)
        await car.save()
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id} not exists')


@router.delete('/{c_id}', response_model=CarSchema, status_code=201, responses=error_response)
async def delete_car(
        c_id: int = Path(..., description='汽车id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of delete one car"""

    car = await Car.get_or_none(id=c_id, is_delete=False)
    if car:
        car.is_delete = False
        await car.save()
        return resp_success(data=car)
    raise NotFound(message=f'Car {c_id}不存在')


@router.post('', response_model=CarSchema, status_code=201, responses=error_response)
async def create_car(parser: CreateCarParser, admin_user: AdminUser = Depends(get_current_admin_user)):
    """the api of create one car"""

    c = await Car.create(**parser.dict())
    return resp_success(data=c)


@router.get('', response_model=ListCarSchema, status_code=200, responses=error_response)
async def list_cars(
        parser: FilterCarParser = Depends(FilterCarParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list cars"""

    params = parser.dict()
    query = filter_cars(params)
    total = await query.count()
    cars = await Car.paginate(query, params['page'], params['pagesize'] or total)

    return resp_success(data={'total': total, 'cars': cars})
