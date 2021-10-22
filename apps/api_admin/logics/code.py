from apps.models import User
from extensions.tools import random_int
from extensions import NotFound
from redis_ext import SMSCodeRedis


async def create_sms_code(params: dict) -> str:
    cellphone = params.get('cellphone')
    user = await User.get_or_none(cellphone=cellphone)
    if user:
        return random_int(length=6)
    raise NotFound(message=f'there is no this user {cellphone}')


async def create_sms_code_task(params: dict, code: str):

    await SMSCodeRedis(key=params.get('cellphone')).set(value=code, ex=60)

    """
    send code to cellphone
    """
