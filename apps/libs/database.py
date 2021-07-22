__all__ = [
    'init_db',
]

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import config


def init_db(app: FastAPI):
    """init and bind tortoise-orm"""

    register_tortoise(
        app,
        config=config.ORM_LINK_CONF
    )
