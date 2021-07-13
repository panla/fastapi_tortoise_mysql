from apps.redis import RedisToolBase


class SMSCodeRedis(RedisToolBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value):
        pool = await self.init()
        await pool.set(self.key, value)
        pool.close()

    async def get(self):
        pool = await self.init()
        rt = await pool.get(self.key)
        pool.close()
        return rt
