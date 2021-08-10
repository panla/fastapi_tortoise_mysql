from fastapi import APIRouter, Depends, Path

from extensions import Route, NotFound, error_response, resp_success
from apps.models import User, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import (
    ReadUserSchema, ListUserSchema, UserSchema, PatchUserParser, FilterCarParser
)
from apps.v1_admin.logics import filter_users, response_users

router = APIRouter(route_class=Route, responses=error_response)


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=200)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read one user"""

    query = await User.get_or_none(id=u_id)

    if query:
        user = query.to_dict()
        user['is_admin_user'] = await query.is_admin_user
        return user
    raise NotFound(message=f'User {u_id} 不存在')


@router.patch('/{u_id}', response_model=UserSchema, status_code=201)
async def patch_user(
        u_id: int = Path(..., description='用户id', ge=1),
        parser: PatchUserParser = Depends(PatchUserParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of update one user"""

    user = await User.get_or_none(id=u_id)
    if user:
        patch_params = dict()
        for k, v in parser.dict().items():
            if v:
                patch_params[k] = v
        await user.update_from_dict(patch_params)
        await user.save()
        return resp_success(data=user)
    raise NotFound(message=f'User {u_id} 不存在')


@router.delete('/{u_id}', response_model=UserSchema, status_code=201)
async def delete_user(
        u_id: int = Path(..., description='用户id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of delete one user"""

    user = await User.get_or_none(id=u_id)
    if user:
        user.is_delete = False
        await user.save()
        return resp_success(data=user)
    raise NotFound(message=f'User {u_id} 不存在')


@router.get('', response_model=ListUserSchema, status_code=200)
async def list_users(
        parser: FilterCarParser = Depends(FilterCarParser),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """the api of read list users"""

    params = parser.dict()
    query = filter_users(params)
    total = await query.count()

    query = User.paginate(query, params['page'], params.get('pagesize') or total)

    users = await response_users(await query)

    return resp_success(data={'total': total, 'users': users})
