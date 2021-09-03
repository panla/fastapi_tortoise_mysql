from apps.v1_admin import entities
import asyncio
import time
import uuid
import typing

from starlette.concurrency import run_in_threadpool


from apps.models import User
from extensions.tools import random_int
from extensions import NotFound, logger


async def create_sms_code(params: dict) -> str:
    cellphone = params.get('cellphone')
    user = await User.get_or_none(cellphone=cellphone)
    if user:
        return random_int(length=6)
    raise NotFound(message=f'there is no this user {cellphone}')


async def create_sms_code_task(params: dict):

    for _ in range(1, 11):
        print(params)

    asyncio.sleep(0.01)
