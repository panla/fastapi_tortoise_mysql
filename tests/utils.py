import json
import random
import string


def read_json_file(path: str):

    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


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
