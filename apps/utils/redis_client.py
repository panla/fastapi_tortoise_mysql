from aioredis import create_redis_pool

import config


class RedisToolBase(object):

    _instance = None

    DB = 0
    PREFIX_KEY = ''

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'

    async def init(self):
        redis_uri = f"redis://:{config.REDIS_PASSWD}@{config.REDIS_HOST}:{config.REDIS_PORT}/{self.DB}?encoding=utf-8"

        pool = SMSCodeRedis._instance or await create_redis_pool(redis_uri)
        SMSCodeRedis._instance = pool
        self.pool = pool


class SMSCodeRedis(RedisToolBase):

    DB = 1
    PREFIX_KEY = 'sms_code:'

    async def set(self, value):
        await self.init()
        await self.pool.set(self.key, value)

    async def get(self, key):
        await self.init()
        return await self.pool.get(self.key)
