from aioredis import create_redis_pool

from config import Config


class RedisToolBase(object):
    _instance = None

    DB = 0
    PREFIX_KEY = ''

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'
        self.redis_uri = 'redis://:{}@{}:{}/{}?encoding=utf-8'.format(
            Config.REDIS_PASSWD, Config.REDIS_HOST, Config.REDIS_PORT, self.DB
        )

    async def init(self):
        self._instance = self._instance or await create_redis_pool(self.redis_uri)
        return self._instance
