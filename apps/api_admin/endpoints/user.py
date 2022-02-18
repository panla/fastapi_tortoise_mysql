from fastapi import APIRouter, Depends, Path

from extensions import Route, Pagination, ErrorSchema
from apps.modules import current_admin_user
from apps.api_admin.schemas import (
    ReadUserSchema, ListUserSchema, UserSchema, PatchUserParser, FilterUserParser
)
from apps.api_admin.logics import UserResolver

router = APIRouter(route_class=Route, responses=ErrorSchema, dependencies=[current_admin_user])


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=200)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1)
):
    """the api of read one user"""

    rt = await UserResolver.read_user(u_id)
    return ReadUserSchema(data=rt)


@router.patch('/{u_id}', response_model=UserSchema, status_code=200)
async def patch_user(
        u_id: int,
        parser: PatchUserParser,
):
    """the api of update one user"""

    user = await UserResolver.patch_user(u_id, parser)
    return UserSchema(data=user)


@router.get('', response_model=ListUserSchema, status_code=200)
async def list_users(
        parser: FilterUserParser = Depends(FilterUserParser)
):
    """the api of read list users"""

    query = UserResolver.list_users(parser)
    total = await query.count()
    query = Pagination(query, parser.page, parser.pagesize).items()
    result = await UserResolver.response_users(await query)

    return ListUserSchema(data={'total': total, 'users': result})
