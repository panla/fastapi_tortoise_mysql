from typing import Union
from datetime import timedelta

from aioredis import Redis

from config import RedisConfig


class BaseRedisClient(object):
    DB = 0
    PREFIX_KEY = ''
    CONNECTION_PARAMS = {'encoding': 'utf-8', 'decode_responses': True}

    def __init__(self) -> None:
        self._key = None
        self.uri = 'redis://:{}@{}:{}/{}'.format(
            RedisConfig.REDIS_PASSWD, RedisConfig.REDIS_HOST, RedisConfig.REDIS_PORT, self.DB
        )
        self.client: Redis = Redis.from_url(self.uri, **self.CONNECTION_PARAMS)

    @property
    def key(self):
        return self._key

    def set_key(self, value):
        self._key = f'{self.PREFIX_KEY}:{value}'

    def get(self):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """

        return self.client.get(self.key)

    def set(self, value, ex: Union[int, timedelta] = None, px: Union[int, timedelta] = None):
        """Set the value at key ``name`` to ``value``

        ``ex`` sets an expired flag on key ``name`` for ``ex`` seconds.
        ``px`` sets an expired flag on key ``name`` for ``px`` milliseconds.
        """

        return self.client.set(name=self._key, value=value, ex=ex, px=px)

    def setnx(self, value):
        """Set the value of key ``name`` to ``value`` if key doesn't exist"""

        return self.client.setnx(name=self._key, value=value)

    def getset(self, value):
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.
        """

        return self.client.getset(name=self._key, value=value)

    def expire(self, seconds):
        """
        Set an expired flag on key ``name`` for ``time`` seconds. ``time``
        can be represented by an integer or a Python timedelta object.
        """

        return self.client.expire(name=self._key, time=seconds)

    def delete(self):
        """Delete one or more keys specified by ``names``"""

        return self.client.delete(self._key)
