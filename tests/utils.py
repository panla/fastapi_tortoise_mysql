import json
import random
import string

from tests import NotFound, User, encode_auth_token


async def authentic_test(cellphone: str):
    user = await User.get_or_none(cellphone=cellphone)
    if not user or user.is_delete:
        raise NotFound(f'User User.cellphone = {cellphone} is not exists or is deleted')

    admin_user = await user.admin_user

    if not admin_user or admin_user.is_delete:
        raise NotFound(message=f'AdminUser User.cellphone = {cellphone} is not exists or is deleted')
    token, login_time, token_expired = encode_auth_token(user.id)
    admin_user.login_time = login_time
    admin_user.token_expired = token_expired
    await admin_user.save()
    return token


def admin_user_test_token():
    return authentic_test(cellphone='10000000001')


def read_json_file(path: str):

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
    :param length: Specified length，default = 4
    :param is_int: whether return int
    :return: Union[str, int]
    """

    all_char = string.digits
    return ''.join(random.sample(all_char, length))
