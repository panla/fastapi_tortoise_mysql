from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import ORM_LINK_CONF


def init_db(app: FastAPI):
    """init and bind tortoise-orm"""

    register_tortoise(app, config=ORM_LINK_CONF)
