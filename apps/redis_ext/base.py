import aioredis

from config import Config


class RedisToolBase(object):
    _client = None

    DB = 0
    PREFIX_KEY = ''

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'
        self.redis_uri = 'redis://:{}@{}:{}/{}?encoding=utf-8'.format(
            Config.REDIS_PASSWD, Config.REDIS_HOST, Config.REDIS_PORT, self.DB
        )

    async def init(self):
        self._client = self._client or aioredis.from_url(self.redis_uri, decode_responses=True)
        return self._client
