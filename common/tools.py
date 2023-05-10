import random
import json
import zipfile
import string
import uuid
from typing import Union
from pathlib import Path

import aiofiles


class FileOperatorBase:

    def __init__(self, path: Union[str, Path]) -> None:
        self.path = path


class FileOperator(FileOperatorBase):

    async def save(self, data):
        async with aiofiles.open(file=self.path, mode='a+', encoding='utf-8') as f:
            await f.write(data)

    async def save_binary(self, data):
        async with aiofiles.open(file=self.path, mode='wb') as f:
            await f.write(data)

    async def read(self):
        async with aiofiles.open(self.path, 'r', encoding='utf-8') as f:
            return await f.read()

    async def read_binary(self):
        async with aiofiles.open(self.path, 'rb') as f:
            return await f.read()


class JsonFileOperator(FileOperatorBase):

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def save(self, data, indent: int = 4):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)


class ZipFileOperator(FileOperatorBase):

    def unzip(self, zip_name: str):
        """unzip -> path/zip_name
        :return: None
        """

        zip_path = Path(self.path).joinpath(zip_name)
        if zipfile.is_zipfile(zip_path):
            try:
                with zipfile.ZipFile(zip_path, 'r') as fz:
                    fz.extractall(zip_path)
            except Exception:
                raise Exception("Unpack the failure")
        else:
            raise Exception("Not a compressed file")

    @staticmethod
    def zip(zip_path: str, dst_path: str, file_list: list):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as fz:
            for filename in file_list:
                fz.write(Path(dst_path).joinpath(filename), filename)
        return zip_path


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

    lis = list()
    for _ in range(length):
        lis.extend(random.choices(all_char, k=1))
    return ''.join(lis)


def random_int(length: int = 4) -> str:
    """
    generate a random str(int) and len == length
    :param length: Specified length，default = 4
    :return: str
    """

    all_char = string.digits
    lis = list()
    for _ in range(length):
        lis.extend(random.choices(all_char, k=1))
    return ''.join(lis)


class UidGenerator:
    """<class 'common.tools.UidGenerator'>"""

    @staticmethod
    def u_id() -> str:
        return f'{random_str(20)}{uuid.uuid4().hex}{random_str(20)}'

    def __str__(self) -> str:
        return self.u_id()

    def __repr__(self) -> str:
        return self.u_id()


def singleton(cls):
    _instance = dict()

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner
