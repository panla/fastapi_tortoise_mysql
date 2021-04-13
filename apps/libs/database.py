from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import config


def init_db(app: FastAPI):
    """绑定 tortoise-orm"""

    register_tortoise(
        app,
        config=config.TORTOISE_ORM
    )
