from tortoise.models import QuerySet

from apps.models import User


def filter_users(params: dict) -> QuerySet:
    """search/filter users"""

    users = User.all()
    if params.get('cellphone'):
        users = users.filter(cellphone__icontains=params['cellphone'])
    return users


async def response_users(users):
    """merge response users"""

    _users = []
    for user in users:
        _user = user.to_dict(selects=['id', 'cellphone', 'name', 'is_delete'])
        _user['is_admin_user'] = await user.is_admin_user
        _users.append(_user)
    return _users
