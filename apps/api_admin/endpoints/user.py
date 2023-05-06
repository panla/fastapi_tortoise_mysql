from fastapi import APIRouter, Depends, Path
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from extensions import Route, ErrorSchema
from apps.modules import current_admin_user
from apps.api_admin.schemas import (
    ReadUserSchema, ListUserSchema, UserSchema, PatchUserParser, FilterUserParser
)
from apps.api_admin.logics import UserResolver

router = APIRouter(route_class=Route, responses=ErrorSchema, dependencies=[current_admin_user])


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=HTTP_200_OK)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1)
):
    """the api of read one user"""

    rt = await UserResolver.read_user(u_id)
    return ReadUserSchema(data=rt)


@router.patch('/{u_id}', response_model=UserSchema, status_code=HTTP_201_CREATED)
async def patch_user(
        u_id: int,
        parser: PatchUserParser,
):
    """the api of update one user"""

    user = await UserResolver.patch_user(u_id, parser)
    return UserSchema(data=user)


@router.get('', response_model=ListUserSchema, status_code=HTTP_200_OK)
async def list_users(
        parser: FilterUserParser = Depends(FilterUserParser)
):
    """the api of read list users"""

    data = await UserResolver.list_users(parser)
    return ListUserSchema(data=data)
