import os
import random
import string
import json
import zipfile
import uuid


class FileOperatorBase:

    def __init__(self, path: str) -> None:
        self.path = path


class FileOperator(FileOperatorBase):

    def save(self, data, mode: str = 'w'):
        with open(self.path, mode, encoding='utf-8') as f:
            f.write(data)

    def save_binary(self, data):
        with open(self.path, 'wb') as f:
            f.write(data)

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()

    def read_binary(self):
        with open(self.path, 'rb') as f:
            return f.read()


class JsonFileOperator(FileOperatorBase):

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data

    def save(self, data, indent: int = 4):
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=indent)


class ZipFileOperator:

    @classmethod
    def unzip(cls, zip_dir: str, zip_name: str):
        """unzip -> path/zip_name
        :return: None
        """

        zip_path = os.path.join(zip_dir, zip_name)
        if zipfile.is_zipfile(zip_path):
            try:
                with zipfile.ZipFile(zip_path, 'r') as fz:
                    fz.extractall(zip_dir)
            except Exception:
                raise Exception("Unpack the failure")
        else:
            raise Exception("Not a compressed file")

    @classmethod
    def zip(cls, zip_path: str, dst_path: str, file_list: list):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip:
            for filename in file_list:
                zip.write(os.path.join(dst_path, filename), filename)
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


class UidGenerator:

    def u_id(self) -> str:
        """len = 72"""

        return f'{random_str(20)}{uuid.uuid4().hex}{random_str(20)}'

    def __str__(self) -> str:
        return self.u_id()

    def __repr__(self) -> str:
        return self.u_id()
