import time
from typing import Tuple, Union
from datetime import timedelta

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

    @property
    def class_name(self):
        return self.__class__.__name__

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

    async def get(self):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """

        rt = await self.client.get(self.key)
        return rt

    async def set(self, value, ex: Union[int, timedelta] = None, px: Union[int, timedelta] = None):
        """Set the value at key ``name`` to ``value``

        ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.
        ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.
        """

        await self.client.set(name=self.key, value=value, ex=ex, px=px)

    async def setnx(self, value):
        """Set the value of key ``name`` to ``value`` if key doesn't exist"""

        await self.client.setnx(name=self.key, value=value)

    async def getset(self, value):
        """
        Sets the value at key ``name`` to ``value``
        and returns the old value at key ``name`` atomically.
        """

        await self.client.getset(name=self.key, value=value)

    async def expire(self, seconds):
        """
        Set an expire flag on key ``name`` for ``time`` seconds. ``time``
        can be represented by an integer or a Python timedelta object.
        """

        await self.client.expire(name=self.key, time=seconds)

    async def delete(self):
        """Delete one or more keys specified by ``names``"""

        await self.client.delete(self.key)


class ResourceLock(RedisClientBase):
    DB = 2
    PREFIX_KEY = 'resource_lock:'
    _timeout = 3600

    async def get_lock(self) -> Tuple[bool, Union[str, None]]:
        """get the lock"""

        current_time = time.time()
        current_value = time.time() + self._timeout

        lock = await self.setnx(current_value)
        if lock:
            await self.expire(self._timeout)
            return True, str(current_value)

        old_lock = await self.get()

        if old_lock and current_time > float(old_lock):
            old_value = await self.getset(current_value)
            if not old_value or old_lock == old_value:
                return True, str(current_value)
            return False, None
        return False, None

    async def del_lock(self):
        """del the lock"""

        await self.delete()

    async def verify_lock(self, value):
        """verify lock"""

        rt = await self.get()
        return bool(rt == value)
