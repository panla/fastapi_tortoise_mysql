__all__ = [
    'random_str', 'random_int',
]

import random
import string


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
