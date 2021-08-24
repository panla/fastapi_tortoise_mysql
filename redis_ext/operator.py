from typing import Union
from datetime import timedelta

from .base import RedisClientBase


class SMSCodeRedis(RedisClientBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value, ex: Union[int, timedelta] = None):
        await self.client.set(name=self.key, value=value, ex=ex)

    async def get(self):
        rt = await self.client.get(self.key)
        return rt
