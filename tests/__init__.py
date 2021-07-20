import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .utils import read_json_file, random_str, random_int
