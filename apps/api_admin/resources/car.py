from fastapi import APIRouter, Depends, Path

from extensions import Route, error_response, resp_success, Pagination
from apps.models import AdminUser
from apps.modules import get_current_admin_user
from apps.api_admin.entities import (
    ReadCarSchema, ListCarSchema, CarSchema, CreateCarParser, PatchCarParser, FilterCarParser
)
from apps.api_admin.logics import CarResolver

router = APIRouter(route_class=Route, responses=error_response)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200)
async def read_car(
        c_id: int = Path(..., description='汽车id', ge=1)
):
    """the api of read one car"""

    car = await CarResolver.read_car(c_id)
    return resp_success(data=car)


@router.patch('/{c_id}', response_model=CarSchema, status_code=201)
async def patch_car(
        c_id: int,
        parser: PatchCarParser,
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of update one car"""

    car = await CarResolver.patch_car(c_id, parser.dict())
    return resp_success(data=car)


@router.post('', response_model=CarSchema, status_code=201)
async def create_car(parser: CreateCarParser, admin_user: AdminUser = Depends(get_current_admin_user)):
    """the api of create one car"""

    c = await CarResolver.create_car(parser.dict())
    return resp_success(data=c)


@router.get('', response_model=ListCarSchema, status_code=200)
async def list_cars(
        parser: FilterCarParser = Depends(FilterCarParser)
):
    """the api of read list cars"""

    payload = parser.dict()

    query = CarResolver.list_cars(payload)
    total = await query.count()
    result = await Pagination(query, payload['page'], payload['pagesize'] or total).result()

    return resp_success(data={'total': total, 'cars': result})
