from tortoise.models import QuerySet

from apps.models import User


def filter_users(params: dict) -> QuerySet:
    """搜索用户"""

    users = User.all()
    if params.get('cellphone'):
        users = users.filter(cellphone__icontains=params['cellphone'])
    return users


async def response_users(users):
    """组合用户列表返回数据"""

    _users = []
    for user in users:
        _user = user.to_dict(selects=['id', 'cellphone', 'name', 'is_delete'])
        _user['is_admin_user'] = await user.is_admin_user
        _users.append(_user)
    return _users
