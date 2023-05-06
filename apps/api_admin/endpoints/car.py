from fastapi import APIRouter, Depends, Path
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from extensions import Route, ErrorSchema
from apps.modules import current_admin_user
from apps.api_admin.schemas import (
    ReadCarSchema, ListCarSchema, CarIDSchema,
    CreateCarParser, PatchCarParser, FilterCarParser
)
from apps.api_admin.logics import CarResolver

router = APIRouter(route_class=Route, responses=ErrorSchema)


@router.get('/{c_id}', response_model=ReadCarSchema, status_code=HTTP_200_OK, dependencies=[current_admin_user])
async def read_car(
        c_id: int = Path(..., description='汽车id', ge=1)
):
    """the api of read one car"""

    data = await CarResolver.read_car(c_id)
    return ReadCarSchema(data=data)


@router.patch(
    '/{c_id}', response_model=CarIDSchema, status_code=HTTP_201_CREATED, dependencies=[current_admin_user]
)
async def patch_car(c_id: int, parser: PatchCarParser):
    """the api of update one car"""

    data = await CarResolver.patch_car(c_id, parser)
    return CarIDSchema(data=data)


@router.post('', response_model=CarIDSchema, status_code=HTTP_201_CREATED, dependencies=[current_admin_user])
async def create_car(parser: CreateCarParser):
    """the api of create one car"""

    data = await CarResolver.create_car(parser)
    return CarIDSchema(data=data)


@router.get('', response_model=ListCarSchema, status_code=HTTP_200_OK)
async def list_cars(parser: FilterCarParser = Depends(FilterCarParser)):
    """the api of read list cars"""

    data = await CarResolver.list_cars(parser)
    return ListCarSchema(data=data)
