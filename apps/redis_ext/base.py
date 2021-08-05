import aioredis

from config import Config


class RedisToolBase(object):
    _client = None

    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'
        self.uri = 'redis://:{}@{}:{}/{}'.format(
            Config.REDIS_PASSWD, Config.REDIS_HOST, Config.REDIS_PORT, self.DB
        )

    @property
    def client(self):
        self._client = self._client or aioredis.from_url(self.uri, **self.CONNECTION_PARAMS)
        return self._client
