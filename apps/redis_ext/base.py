import aioredis

from config import Config


class RedisClientBase(object):
    _client = None

    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'
        self.uri = 'redis://:{}@{}:{}/{}'.format(
            Config.REDIS_PASSWD, Config.REDIS_HOST, Config.REDIS_PORT, self.DB
        )
        self.client = self._get_client()
        self._client = self.client

    def _get_client(self):
        return self._client or aioredis.from_url(self.uri, **self.CONNECTION_PARAMS)
