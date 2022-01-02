from fastapi import APIRouter, Depends, Path

from extensions import Route, Pagination, resp_success
from conf.define import error_schema
from apps.modules import current_admin_user
from apps.api_admin.entities import (
    ReadUserSchema, ListUserSchema, UserSchema, PatchUserParser, FilterUserParser
)
from apps.api_admin.logics import UserResolver

router = APIRouter(route_class=Route, responses=error_schema, dependencies=[current_admin_user])


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=200)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1)
):
    """the api of read one user"""

    rt = await UserResolver.read_user(u_id)
    return resp_success(data=rt)


@router.patch('/{u_id}', response_model=UserSchema, status_code=201)
async def patch_user(
        u_id: int,
        parser: PatchUserParser,
):
    """the api of update one user"""

    user = await UserResolver.patch_user(u_id, parser)
    return resp_success(data=user)


@router.get('', response_model=ListUserSchema, status_code=200)
async def list_users(
        parser: FilterUserParser = Depends(FilterUserParser)
):
    """the api of read list users"""

    query = UserResolver.list_users(parser)
    total = await query.count()
    query = Pagination(query, parser.page, parser.pagesize).items()
    result = await UserResolver.response_users(await query)

    return resp_success(data={'total': total, 'users': result})
