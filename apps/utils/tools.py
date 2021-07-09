import random
from typing import Union

__all__ = [
    'random_str', 'random_int',
]


def random_str(length: int = 20, has_num: bool = False) -> str:
    """
    生成指定长度的随机字符串
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
    """
    生成指定长度的随机数字组成的字符串
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
