"""
write data into database

python tools/insert_into.py --help

JSON file
    example
    [
        {
            "id": 1,
            "name": "1"
            ...
        }
    ]
"""

import argparse
import json
import sys
import traceback
from typing import List
from pathlib import Path

from tortoise import Tortoise, run_async
from tortoise.transactions import atomic

BASEDIR = Path(__file__).parent.parent

sys.path.append(BASEDIR.name)

from config import ORM_LINK_CONF
from apps.models import models as models_file

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, required=True, help='JSON File Path')
parser.add_argument('-m', '--model', type=str, required=True, help='Model Class Str')
parser.add_argument('-b', '--batch_size', type=int, required=False, default=5, help='Batch Size')

params = parser.parse_args().__dict__
file_path = params.get('file')
ModelClassStr = params.get('model')
batch_size = params.get('batch_size')

if not Path(file_path).is_file():
    sys.stderr.write(f'parameter -f/--file error: {file_path} not exists')
    sys.exit(1)

if not getattr(models_file, ModelClassStr):
    sys.stderr.write(f'parameter -m/--model error: {ModelClassStr} not exists')
    sys.exit(1)

if batch_size <= 0:
    sys.stderr.write(f'parameter -b/--batch_size error: {batch_size} <= 0')
    sys.exit(1)


def build_instances(model_class, dic_list: List[dict]):
    """create some Model instance"""

    rt = []
    for per_dic in dic_list:
        rt.append(model_class(**per_dic))
    return rt


def read_json_file(path: str) -> List[dict]:
    """read json file and return dict"""

    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


@atomic()
async def create_data():
    try:
        model_class = getattr(models_file, ModelClassStr)
        origin_data = read_json_file(file_path)
        await getattr(model_class, 'bulk_create')(
            objects=build_instances(model_class, origin_data), batch_size=batch_size
        )
        sys.stdout.write('create data over\n')
    except Exception as exc:
        sys.stdout.write(f'{exc}\n')
        sys.stdout.write(f'{traceback.format_exc()}\n')


async def main():
    await Tortoise.init(config=ORM_LINK_CONF)

    await create_data()


if __name__ == '__main__':
    run_async(main())
