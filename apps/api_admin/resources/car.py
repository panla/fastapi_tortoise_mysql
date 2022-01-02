from fastapi import APIRouter, Depends, Path

from extensions import Route, Pagination, resp_success
from conf.define import error_schema
from apps.modules import current_admin_user
from apps.api_admin.entities import (
    ReadCarSchema, ListCarSchema, CarIDSchema,
    CreateCarParser, PatchCarParser, FilterCarParser
)
from apps.api_admin.logics import CarResolver

router = APIRouter(route_class=Route, responses=error_schema)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=200)
async def read_car(
        c_id: int = Path(..., description='汽车id', ge=1)
):
    """the api of read one car"""

    car = await CarResolver.read_car(c_id)
    return resp_success(data=car)


@router.patch('/{c_id}', response_model=CarIDSchema, status_code=201, dependencies=[current_admin_user])
async def patch_car(c_id: int, parser: PatchCarParser):
    """the api of update one car"""

    car = await CarResolver.patch_car(c_id, parser)
    return resp_success(data=car)


@router.post('', response_model=CarIDSchema, status_code=201, dependencies=[current_admin_user])
async def create_car(parser: CreateCarParser):
    """the api of create one car"""

    c = await CarResolver.create_car(parser)
    return resp_success(data=c)


@router.get('', response_model=ListCarSchema, status_code=200)
async def list_cars(parser: FilterCarParser = Depends(FilterCarParser)):
    """the api of read list cars"""

    payload = parser.dict()

    query = CarResolver.list_cars(payload)
    total = await query.count()
    result = await Pagination(query, payload['page'], payload['pagesize'] or total).items()

    return resp_success(data={'total': total, 'cars': result})
