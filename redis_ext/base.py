import os
import threading
from datetime import timedelta
from typing import Union, Optional

from redis.asyncio import Redis
from redis.asyncio.connection import ConnectionPool

from config import RedisConfig
from conf.const import EnvConst

REDIS_CONNECTION_PARAMS = {
    'host': RedisConfig.HOST,
    'port': RedisConfig.PORT,
    'password': RedisConfig.PASSWD,
    'socket_timeout': RedisConfig.SOCKET_TIMEOUT,
    'socket_connect_timeout': RedisConfig.SOCKET_CONNECT_TIMEOUT,
    'socket_keepalive': True,
    'encoding': 'utf-8',
    'decode_responses': True,
    'max_connections': RedisConfig.MAX_CONNECTIONS,
    'username': RedisConfig.USER
}


class Pool:
    cache = dict()
    lock = threading.Lock()
    instance = None

    def __init__(self, db: int = 0) -> None:
        self.db = db

    def __new__(cls, db: int = 0):
        db = str(db)

        with cls.lock:
            if not cls.instance:
                cls.instance = super().__new__(cls)

            if not cls.cache.get(db):
                cls.cache[db] = ConnectionPool(db=db, **REDIS_CONNECTION_PARAMS)

            return cls.instance

    def pool(self):
        return self.cache.get(str(self.db))


class BaseRedis(object):
    DB = 0
    PREFIX_KEY = ''

    def __init__(self) -> None:
        self._name = None

        # TODO FIX
        if os.environ.get('CODE_ENV') == EnvConst.TEST:
            self.client: Redis = Redis(connection_pool=ConnectionPool(db=self.DB, **REDIS_CONNECTION_PARAMS))
        else:
            self.client: Redis = Redis(connection_pool=Pool(self.DB).pool())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = f'{self.PREFIX_KEY}:{value}'

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
        """Returns the number of ``names`` that exist"""

        return self.client.exists(self.name)

    def get(self):
        """
        Return the value at key ``name``, or None if the key doesn't exist
        """

        return self.client.get(name=self.name)

    def incr_by(self, amount: int = 1):
        """value += amount"""

        return self.client.incrby(name=self.name, amount=amount)

    def set(
            self,
            value,
            ex: Union[int, timedelta] = None,
            px: Union[int, timedelta] = None,
            nx: bool = False,
            xx: bool = False,
            get: bool = False
    ):
        """Set the value at key ``name`` to ``value``

        ``ex`` sets an expired flag on key ``name`` for ``ex`` seconds.

        ``px`` sets an expired flag on key ``name`` for ``px`` milliseconds.

        ``nx`` if set to True, set the value at key ``name`` to ``value`` only
            if it does not exist.

        ``xx`` if set to True, set the value at key ``name`` to ``value`` only
            if it already exists.

        ``get`` if True, set the value at key ``name`` to ``value`` and return
            the old value stored at key, or None if the key did not exist.
            (Available since Redis 6.2)
        """

        return self.client.set(name=self.name, value=value, ex=ex, px=px, nx=nx, xx=xx, get=get)

    def set_nx(self, value):
        """Set the value of key ``name`` to ``value`` if key doesn't exist"""

        return self.client.setnx(name=self.name, value=value)

    def hash_set(self, key: Optional[str] = None, value: Optional[str] = None, mapping: Optional[dict] = None):
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that that will be
        added to hash ``name``.
        Returns the number of fields that were added.
        """

        return self.client.hset(name=self.name, key=key, value=value, mapping=mapping)

    def hash_get(self, key):
        """hash, Return the value of ``key`` within the hash ``name``"""

        return self.client.hget(name=self.name, key=key)

    def hash_get_all_values(self):
        """hash, Return a Python dict of the hash's name/value pairs"""

        return self.client.hgetall(name=self.name)

    def hash_del_key(self, keys: list):
        """hash, Delete ``keys`` from hash ``name``

        have * need list         ([key, key, key])
        no   * need multiple key (key, key, key)
        """

        self.client.hdel(self.name, *keys)

    def list_right_push(self, values: list):
        """list, Push ``values`` onto the tail of the list ``name``"""

        return self.client.rpush(self.name, *values)

    def list_left_range(self, start: int = 0, end: int = -1):
        """list, Return a slice of the list ``name`` between position ``start`` and ``end``"""

        return self.client.lrange(name=self.name, start=start, end=end)

    def list_set(self, index, value):
        """list, Set element at ``index`` of list ``name`` to ``value``"""

        return self.client.lset(name=self.name, index=index, value=value)
