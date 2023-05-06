from extensions import Pagination
from apps.modules import ResourceOp
from apps.models import User
from apps.api_admin.schemas import FilterUserParser, PatchUserParser


class UserResolver:

    @classmethod
    async def list_users(cls, parser: FilterUserParser) -> dict:
        """search/filter users"""

        query = User.all()
        if parser.cellphone:
            query = query.filter(cellphone__icontains=parser.cellphone)

        total = await query.count()
        query = Pagination(query, parser.page, parser.page_size).items()
        result = await UserResolver.response_users(await query)

        return {'total': total, 'users': result}

    @classmethod
    async def patch_user(cls, user_id: int, parser: PatchUserParser):
        """update user"""

        instances, _ = await ResourceOp(User, user_id).instance()

        patch_params = dict()
        for k, v in parser.dict().items():
            if v is not None:
                patch_params[k] = v
        if patch_params:
            await instances.update(**patch_params)

        return await instances.first()

    @classmethod
    async def response_users(cls, users):
        """merge response users"""

        _users = list()
        for user in users:
            _user = User.to_dict(user, selects=('id', 'cellphone', 'name', 'is_delete'))
            _user['is_admin_user'] = await user.is_admin_user
            _users.append(_user)
        return _users

    @classmethod
    async def read_user(cls, user_id: int):

        _, instance = await ResourceOp(User, user_id).instance(is_delete=False)

        user = User.to_dict(instance)
        user['is_admin_user'] = await instance.is_admin_user
        return user
