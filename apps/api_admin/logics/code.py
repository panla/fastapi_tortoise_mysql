import asyncio

from extensions import NotFound, BadRequest
from common.tools import random_int
from redis_ext import SMSCodeRedis
from apps.models import User
from apps.api_admin.entities import CreateCodeParser


async def create_sms_code(parser: CreateCodeParser) -> str:
    cellphone = parser.cellphone
    user = await User.get_or_none(cellphone=cellphone)
    if user:
        # long key
        sms_redis_op = SMSCodeRedis(f'{cellphone}-{cellphone}')
        if await sms_redis_op.get():
            raise BadRequest(message='Request too fast!')

        code = random_int(length=6)

        # long key
        await sms_redis_op.set(value=code, ex=20)

        # short key
        sms_redis_op = SMSCodeRedis(cellphone)
        await sms_redis_op.set(value=code, ex=60)

        return code
    else:
        del user
        raise NotFound(message=f'there is no this user {cellphone}')


async def send_sms_task(parser: CreateCodeParser, code: str):

    await asyncio.sleep(10)

    """
    send code to cellphone
    """
