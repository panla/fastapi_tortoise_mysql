from tortoise.models import QuerySet

from apps.models import User


def filter_users(params: dict) -> QuerySet:
    """搜索用户"""

    users = User.all()
    if params.get('cellphone'):
        users = users.filter(cellphone__icontains=params['cellphone'])
    return users
