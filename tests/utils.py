import sys
import json
import random
import string

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
    return authentic_test(cellphone='10000000001')


def read_json_file(path: str):
    """读取JSON文件
    :param path: JSON文件路径
    :return dict
    """

    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def random_str(length: int = 20, has_num: bool = False) -> str:
    """
    generate a random str and len == length
    :param length: the random str`length, default=20
    :param has_num: has int?
    :return: str
    """

    all_char = string.ascii_lowercase + string.ascii_uppercase
    if has_num:
        all_char += string.digits

    return ''.join(random.sample(all_char, length))


def random_int(length: int = 4) -> str:
    """
    generate a random str/int and len == length
    :param length: 指定的长度，默认4
    :param is_int: 是否返回整型
    :return: Union[str, int]
    """

    all_char = string.digits
    return ''.join(random.sample(all_char, length))
