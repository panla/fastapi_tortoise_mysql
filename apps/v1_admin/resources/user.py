from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path

from apps.extensions import Route, NotFound, error_response
from apps.utils import resp_success
from apps.models import User, AdminUser
from apps.modules import get_current_admin_user
from apps.v1_admin.entities import ReadUserSchema, ListUserSchema, UserSchema
from apps.v1_admin.entities import PatchUserParams
from apps.v1_admin.entities import filter_user_dependency
from apps.v1_admin.logics import filter_users, response_users

router = APIRouter(route_class=Route)


@router.get('/{u_id}', response_model=ReadUserSchema, status_code=200, responses=error_response)
async def read_user(
        u_id: int = Path(..., description='用户id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """用户详情接口"""

    query = await User.get_or_none(id=u_id)

    if query:
        user = query.to_dict()
        user['is_admin_user'] = await query.is_admin_user
        return user
    raise NotFound(message=f'User {u_id} 不存在')


@router.patch('/{u_id}', response_model=UserSchema, status_code=201, responses=error_response)
async def patch_user(u_id: int, params: PatchUserParams, admin_user: AdminUser = Depends(get_current_admin_user)):
    """更新用户"""

    assert u_id > 0, f'u_id is {u_id}, it needs > 0'

    user = await User.get_or_none(id=u_id)
    if user:
        patch_params = dict()
        for k, v in params.dict().items():
            if v:
                patch_params[k] = v
        await user.update_from_dict(patch_params)
        await user.save()
        return resp_success(data=user)
    raise NotFound(message=f'User {u_id} 不存在')


@router.delete('/{u_id}', response_model=UserSchema, status_code=201, responses=error_response)
async def delete_user(
        u_id: int = Path(..., description='用户id', ge=1),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """删除用户"""

    user = await User.get_or_none(id=u_id)
    if user:
        user.is_delete = False
        await user.save()
        return resp_success(data=user)
    raise NotFound(message=f'User {u_id} 不存在')


@router.get('', response_model=ListUserSchema, status_code=200, responses=error_response)
async def list_users(
        params: dict = Depends(filter_user_dependency),
        admin_user: AdminUser = Depends(get_current_admin_user)
):
    """用户列表接口"""

    query = filter_users(params)
    total = await query.count()

    query = User.paginate(query, params['page'], params.get('pagesize') or total)

    users = await response_users(await query)

    return resp_success(data={'total': total, 'users': users})
