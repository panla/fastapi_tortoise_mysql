import sys

from tests import BASE_DIR

sys.path.append(BASE_DIR)

from apps.extensions import NotFound
from apps.models import User, AdminUser
from apps.modules.token import encode_auth_token


async def authentic_test(cellphone: str):
    user = await User.get_or_none(cellphone=cellphone)
    if not user or user.is_delete:
        raise NotFound(message=f'User {cellphone} 不存在或被删除')
    admin_user = await AdminUser.get_or_none(user_id=user.id)
    if not admin_user or admin_user.is_delete:
        raise NotFound(message=f'AdminUser {cellphone} 不存在或被删除')
    token, login_time, token_expired = encode_auth_token(user.id)
    admin_user.login_time = login_time
    admin_user.token_expired = token_expired
    await admin_user.save()
    return token


def admin_user_test_token():
    return authentic_test(cellphone='12345678911')
