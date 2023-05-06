import asyncio
import os
import sys
import json
from pathlib import Path
from typing import Union, List
from functools import wraps
from datetime import datetime

import click
from tortoise import Tortoise
from tortoise.transactions import atomic
from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from config import ORM_LINK_CONF
from apps.models import User, Book, AdminUser, Car, Order, Phone, Question

model_map = {
    'User': User,
    'Book': Book,
    'AdminUser': AdminUser,
    'Car': Car,
    'Order': Order,
    'Phone': Phone,
    'Question': Question
}


def _read_json_file(path: str) -> List[dict]:
    """read json file and return dict"""

    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())


def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(f(*args, **kwargs))
        finally:
            if f.__name__ != "cli":
                loop.run_until_complete(Tortoise.close_connections())

    return wrapper


async def create(model, params: List[dict]):
    for param in params:
        instance = await model.get_or_none(id=param.get('id'))
        if instance:
            await instance.update_from_dict(param)
            await instance.save()
        else:
            instance = await model.create(**param)


@click.group()
@click.pass_context
@coro
async def cli(ctx: click.Context):
    await Tortoise.init(config=ORM_LINK_CONF)


@click.command(help='create init data')
@click.pass_context
@click.option('-f', '--file', type=str, required=True, help='json file')
@click.option('-m', '--model', type=str, required=True, help='Database Model')
@coro
@atomic()
async def init_data(ctx: click.Context, file: str, model: str):
    """create users"""

    model_class = model_map.get(model)
    if not model_class:
        raise Exception(f'no this Model {model}')

    params = _read_json_file(file)

    await create(model_class, params)
    logger.info('create users over')


@click.command(help='create migration template file')
@click.pass_context
@click.option('-d', '--migration_dir', type=str, required=True, help='Migration Dir')
@click.option('-n', '--migration_name', type=str, required=True, help='Migration Name')
def create_migration_file(ctx: click.Context, migration_dir: str, migration_name: str):
    """create a blank migration sql file"""

    migration_dir_p = Path(migration_dir)
    if not migration_dir_p.is_dir():
        migration_dir_p.mkdir(exist_ok=True)

    now = datetime.now().strftime('%Y%m%d%H%M%S')

    # get the new latest sql file index
    exists_sql_file_names = os.listdir(migration_dir_p)
    if exists_sql_file_names:
        latest_sql_file_index = max([int(f.split(bytes('_'))[0]) for f in exists_sql_file_names])
        new_latest_sql_file_index = latest_sql_file_index + 1
    else:
        new_latest_sql_file_index = 0

    # get the new latest sql file name
    new_latest_sql_file_name = f'{new_latest_sql_file_index}_{now}_{migration_name}.sql'

    data = """-- upgrade --

    -- downgrade --

    """

    with open(migration_dir_p.joinpath(new_latest_sql_file_name), 'w', encoding='utf-8') as f:
        f.write(data)

    logger.info(f'create {migration_name} done')


@click.command(help='find some target data')
@click.pass_context
@click.option('-d', '--dirs', nargs='*', type=str, required=True, help='dirs')
@click.option('-t', '--targets', nargs='+', required=True, help='target')
def find(ctx: click.Context, dirs: list, targets: list):
    """
    Traverse all files under single or multiple folders (UTF-8 files)
    Find the target in the file according to the targets in the parameter
    If found, record the target and file path in the log
    """

    directions = list()

    if dirs:
        for d in dirs:
            _d = Path(d).absolute()
            if _d.is_dir():
                directions.append(_d)
    else:
        logger.error(f'your input -d/--dirs {dirs} error')
        return

    if not directions:
        logger.error(f'your input -d/--dirs {directions} error')
        return

    if not targets:
        logger.error(f'your input -t/--targets {targets} error')
        return

    def read_file(path: Union[str, Path]) -> str:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except:
            return ''

    for direction in directions:
        for root, _, files in os.walk(direction):
            for file in files:
                file_path = Path(root, file)
                txt = read_file(file_path)
                for target in targets:
                    if target in txt:
                        logger.info(f'{file_path}')

    logger.info('find done')


cli.add_command(init_data)
cli.add_command(create_migration_file)

if __name__ == '__main__':
    cli()
