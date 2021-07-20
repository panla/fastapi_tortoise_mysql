import sys
import json
import random
from typing import Union

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
    """生成指定长度的随机字符串
    :param length: 指定的长度，默认20
    :param has_num: 是否包含数字
    :return: str
    """

    lis = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    if has_num:
        lis += ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    results = []
    for i in range(length):
        results += random.choices(lis)
    return ''.join(results)


def random_int(length: int = 4, is_int: bool = False) -> Union[str, int]:
    """生成指定长度的随机数字组成的字符串
    :param length: 指定的长度，默认4
    :param is_int: 是否返回整型
    :return: Union[str, int]
    """

    lis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    results = []
    for i in range(length):
        results += random.choices(lis)
    results = ''.join(results)
    if is_int:
        return int(results)
    return results
