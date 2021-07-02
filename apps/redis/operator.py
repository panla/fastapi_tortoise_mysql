from apps.redis import RedisToolBase


class SMSCodeRedis(RedisToolBase):

    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value):
        self.pool or await self.init()
        await self.pool.set(self.key, value)

    async def get(self):
        self.pool or await self.init()
        return await self.pool.get(self.key)
