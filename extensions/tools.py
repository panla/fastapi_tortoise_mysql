import os
import random
import string
import json
import zipfile


class FileOperatorBase:

    def __init__(self, path: str) -> None:
        self.path = path


class FileOperator(FileOperatorBase):

    def save(self, data, filename: str):

        return data.save(os.path.join(self.path, filename))

    def read_binary(self):
        with open(self.path, 'rb') as f:
            return f.read()

    def read(self):

        with open(self.path, 'r', encoding='utf-8') as f:
            return f.read()


class ZipFileOperator(FileOperatorBase):

    def unzip(self, zip_name: str):
        """unzip -> path/zip_name
        :return: None
        """

        zip_path = os.path.join(self.path, zip_name)
        if zipfile.is_zipfile(zip_path):
            try:
                fz = zipfile.ZipFile(zip_path, 'r')
                for file in fz.namelist():
                    fz.extract(file, self.path)
            except Exception:
                raise Exception("Unpack the failure")
        else:
            raise Exception("Not a compressed file")

    def zip(self, zip_path: str, dst_path: str, file_list: list):
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip:
            for filename in file_list:
                zip.write(os.path.join(dst_path, filename), filename)
        return zip_path


class JsonFileOperator(FileOperatorBase):

    def read(self):
        with open(self.path, 'r', encoding='utf-8') as fi:
            data = json.load(fi)
        return data

    def write(self, data):
        with open(self.path, 'w', encoding='utf-8') as fi:
            json.dump(data, fi, ensure_ascii=False, indent=4)


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
