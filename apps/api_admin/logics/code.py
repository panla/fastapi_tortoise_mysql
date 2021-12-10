import asyncio

from extensions import NotFound, BadRequest, random_int
from redis_ext import SMSCodeRedis
from apps.models import User


async def create_sms_code(params: dict) -> str:
    cellphone = params.get('cellphone')
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


async def send_sms_task(params: dict, code: str):

    await asyncio.sleep(10)

    """
    send code to cellphone
    """
