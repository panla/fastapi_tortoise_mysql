from typing import Union
from datetime import timedelta

from aioredis.client import Redis
from aioredis.connection import ConnectionPool

from config import RedisConfig

REDIS_CONNECTION_PARAMS = {
    'max_connections': RedisConfig.MAX_CONNECTIONS,
    'username': RedisConfig.USER,
    'password': RedisConfig.PASSWD,
    'host': RedisConfig.HOST,
    'port': RedisConfig.PORT,
    'encoding': 'utf-8',
    'decode_responses': True
}
REDIS_POOL_CACHE = dict()


def make_pool(db: int = 0):
    global REDIS_POOL_CACHE

    pool = REDIS_POOL_CACHE.get(str(db))
    if pool:
        return pool
    else:
        pool = ConnectionPool(db=db, **REDIS_CONNECTION_PARAMS)
        REDIS_POOL_CACHE[str(db)] = pool
        return pool


class BaseRedis(object):
    DB = 0
    PREFIX_KEY = ''

    def __init__(self) -> None:
        self._name = None
        self.client: Redis = Redis(connection_pool=make_pool(db=self.DB))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = f'{self.PREFIX_KEY}:{value}'

    def get(self):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """

        return self.client.get(name=self.name)

    def set(self, value, ex: Union[int, timedelta] = None, px: Union[int, timedelta] = None):
        """Set the value at key ``name`` to ``value``

        ``ex`` sets an expired flag on key ``name`` for ``ex`` seconds.
        ``px`` sets an expired flag on key ``name`` for ``px`` milliseconds.
        """

        return self.client.set(name=self.name, value=value, ex=ex, px=px)

    def set_nx(self, value):
        """Set the value of key ``name`` to ``value`` if key doesn't exist"""

        return self.client.setnx(name=self.name, value=value)

    def getset(self, value):
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.
        """

        return self.client.getset(name=self.name, value=value)

    def set_kv(self, key, value):
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that that will be
        added to hash ``name``.
        Returns the number of fields that were added.
        """

        return self.client.hset(name=self.name, key=key, value=value)

    def get_kv(self, key):
        """Return the value of ``key`` within the hash ``name``"""

        return self.client.hget(name=self.name, key=key)

    def set_mapping(self, mapping: dict):
        """
        Set key to value within hash ``name`` for each corresponding
        key and value from the ``mapping`` dict.
        """

        return self.client.hmset(name=self.name, mapping=mapping)

    def get_all_values(self):
        """Return a Python dict of the hash's name/value pairs"""

        return self.client.hgetall(name=self.name)

    def expire(self, seconds):
        """
        Set an expired flag on key ``name`` for ``time`` seconds. ``time``
        can be represented by an integer or a Python timedelta object.
        """

        return self.client.expire(name=self.name, time=seconds)

    def delete(self):
        """Delete one or more keys specified by ``names``"""

        return self.client.delete(self.name)

    def exists(self):
        return self.client.exists(self.name)
