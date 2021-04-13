from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import tortoise_conf


def init_db(app: FastAPI):
    """绑定 tortoise-orm"""

    register_tortoise(
        app,
        config=tortoise_conf.TORTOISE_ORM
    )
