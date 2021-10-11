from tortoise.models import QuerySet

from apps.modules import ResourceOp
from apps.models import User


class UserResolver:

    @classmethod
    def list_users(cls, params: dict) -> QuerySet:
        """search/filter users"""

        query = User.all()
        if params.get('cellphone'):
            query = query.filter(cellphone__icontains=params['cellphone'])
        return query

    @classmethod
    async def patch_user(cls, user_id: int, params: dict):
        user = await ResourceOp(User, user_id).instance()

        patch_params = dict()
        for k, v in params.items():
            if v:
                patch_params[k] = v
        if patch_params:
            user = await user.update_from_dict(patch_params)
            await user.save()
        return user

    @classmethod
    async def response_users(cls, users) -> list:
        """merge response users"""

        _users = []
        for user in users:
            _user = User.to_dict(user, selects=('id', 'cellphone', 'name', 'is_delete'))
            _user['is_admin_user'] = await user.is_admin_user
            _users.append(_user)
        return _users

    @classmethod
    async def read_user(cls, user_id: int):
        query = await ResourceOp(User, user_id).instance(is_delete=False)

        user = User.to_dict(query)
        user['is_admin_user'] = await query.is_admin_user
        return user
