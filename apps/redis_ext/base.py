from aioredis import Redis, from_url

from config import Config


REDIS_CLIENT_CACHE = {}


class RedisClientBase(object):
    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self, key) -> None:
        self.key = f'{self.PREFIX_KEY}{key}'

        self.uri = 'redis://:{}@{}:{}/{}'.format(
            Config.REDIS_PASSWD, Config.REDIS_HOST, Config.REDIS_PORT, self.DB
        )

    # @property
    # def client(self) -> Redis:
    #     """make sure one class, one instance

    #     whether it is good or bad?
    #     """

    #     client = REDIS_CLIENT_CACHE.get(self.class_name) or from_url(self.uri, **self.CONNECTION_PARAMS)
    #     REDIS_CLIENT_CACHE[self.class_name] = client
    #     return client

    @property
    def client(self) -> Redis:
        return from_url(self.uri, **self.CONNECTION_PARAMS)

    @property
    def class_name(self):
        return self.__class__.__name__
