from fastapi import APIRouter, Depends, Path

from extensions import Route, error_response, resp_success, Pagination
from apps.models import AdminUser
from apps.modules import get_current_admin_user
from apps.api_admin.entities import (
    ReadUserSchema, ListUserSchema, UserSchema, PatchUserParser, FilterUserParser
)
from apps.api_admin.logics import UserResolver

router = APIRouter(route_class=Route, responses=error_response)


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=200)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read one user"""

    rt = await UserResolver.read_user(u_id)
    return resp_success(data=rt)


@router.patch('/{u_id}', response_model=UserSchema, status_code=201)
async def patch_user(
        u_id: int,
        parser: PatchUserParser,
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of update one user"""

    user = await UserResolver.patch_user(u_id, parser.dict())
    return resp_success(data=user)


@router.get('', response_model=ListUserSchema, status_code=200)
async def list_users(
        parser: FilterUserParser = Depends(FilterUserParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list users"""

    payload = parser.dict()

    query = UserResolver.list_users(payload)
    total = await query.count()
    query = Pagination(query, payload['page'], payload.get('pagesize') or total).result()
    result = await UserResolver.response_users(await query)

    return resp_success(data={'total': total, 'users': result})
