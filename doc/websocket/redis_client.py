import aioredis


class RedisClient(object):
    _client = None

    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'
        self.uri = 'redis://:{}@{}:{}/{}'.format(
            '', '127.0.0.1', 6379, self.DB
        )

        self.client = self._get_client()
        self._client = self.client

    def _get_client(self):
        return self._client or aioredis.from_url(self.uri, **self.CONNECTION_PARAMS)

    async def get(self):
        rt = await self.client.get(self.key)
        return rt

    async def lpop(self):
        rt = await self.client.lpop(self.key)
        return rt
