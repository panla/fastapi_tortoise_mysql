import asyncio

from extensions import NotFound, BadRequest
from common import random_int
from services.redis_ext import SMSCodeRedis
from apps.models import User
from apps.api_admin.schemas import CreateCodeParser


async def create_sms_code(parser: CreateCodeParser):
    cellphone = parser.cellphone
    user = await User.get_or_none(cellphone=cellphone)
    if user:
        # long key
        sms_redis_op = SMSCodeRedis()
        sms_redis_op.name = f'{cellphone}-{cellphone}'
        if await sms_redis_op.get():
            raise BadRequest(message='Request too fast!')

        code = random_int(length=6)

        # long key
        await sms_redis_op.set(value=code, ex=20)

        # short key
        sms_redis_op.name = cellphone
        await sms_redis_op.set(value=code, ex=60)

        return {'success': True, 'code': code}
    else:
        del user
        raise NotFound(message=f'there is no this user {cellphone}')


async def send_sms_task(parser: CreateCodeParser, code: str):

    await asyncio.sleep(10)

    """
    send code to cellphone
    """
