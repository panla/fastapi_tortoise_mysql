from .base import RedisClientBase


class SMSCodeRedis(RedisClientBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value):
        await self.client.set(self.key, value)

    async def get(self):
        rt = await self.client.get(self.key)
        return rt
