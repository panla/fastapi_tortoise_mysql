from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import config

__all__ = [
    'init_db',
]


def init_db(app: FastAPI):
    """绑定 tortoise-orm"""

    register_tortoise(
        app,
        config=config.TORTOISE_ORM
    )
