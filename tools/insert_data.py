import asyncio
import sys
import json
from pathlib import Path
from typing import List
from functools import wraps

import click
from tortoise import Tortoise
from tortoise.transactions import atomic
from loguru import logger

BASEDIR = Path(__file__).parent.parent

sys.path.append(BASEDIR.name)

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
@click.argument('-f', '--file', help='json file')
@click.argument('-m', '--model', help='Database Model')
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


cli.add_command(init_data)

if __name__ == '__main__':
    cli()
