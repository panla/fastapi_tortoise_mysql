from aioredis import from_url, Redis


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

    @property
    def client(self) -> Redis:
        return from_url(self.uri, **self.CONNECTION_PARAMS)

    async def get(self):
        rt = await self.client.get(self.key)
        return rt

    async def lpop(self):
        rt = await self.client.lpop(self.key)
        return rt
