__all__ = [
    'random_str', 'random_int',
]

import random
from typing import Union


def random_str(length: int = 20, has_num: bool = False) -> str:
    """
    generate a random str and len == length
    :param length: the random str`length, default=20
    :param has_num: has int?
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
    """
    generate a random str/int and len == length
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
