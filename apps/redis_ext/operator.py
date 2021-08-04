from .base import RedisToolBase


class SMSCodeRedis(RedisToolBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value):
        client = await self.init()
        await client.set(self.key, value)

    async def get(self):
        client = await self.init()
        rt = await client.get(self.key)
        return rt
