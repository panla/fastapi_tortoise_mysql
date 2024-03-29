import os
from typing import Union, Optional

from redis.typing import EncodableT, ExpiryT
from redis.asyncio import Redis
from redis.asyncio.connection import ConnectionPool

from config import RedisConfig
from conf import EnvConst
from common import singleton

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


@singleton
class Pool:
    def __init__(self, db: int = 0) -> None:
        self.db = ConnectionPool(db=db, **REDIS_CONNECTION_PARAMS)

    def pool(self):
        return self.db


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

    def expire(self, seconds: ExpiryT, nx: bool = False, xx: bool = False, gt: bool = False, lt: bool = False):
        """
        Set an expired flag on key ``name`` for ``time`` seconds. ``time``
        can be represented by an integer or a Python timedelta object.

            NX -> Set expiry only when the key has no expiry
            XX -> Set expiry only when the key has an existing expiry
            GT -> Set expiry only when the new expiry is greater than current one
            LT -> Set expiry only when the new expiry is less than current one
        """

        return self.client.expire(name=self.name, time=seconds, nx=nx, xx=xx, gt=gt, lt=lt)

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

    def _incr_by(self, amount: int = 1):
        """value += amount"""

        return self.client.incrby(name=self.name, amount=amount)

    def set(
            self,
            value: EncodableT,
            ex: Union[ExpiryT, None] = None,
            px: Union[ExpiryT, None] = None,
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

    def _hash_set(self, key: Optional[str] = None, value: Optional[str] = None, mapping: Optional[dict] = None):
        """
        Set ``key`` to ``value`` within hash ``name``,
        ``mapping`` accepts a dict of key/value pairs that that will be
        added to hash ``name``.
        Returns the number of fields that were added.
        """

        return self.client.hset(name=self.name, key=key, value=value, mapping=mapping)

    async def _hash_get_values(self, keys: list = None):
        """hash, Returns a list of values ordered identically to ``keys``"""

        if not keys:
            return await self.client.hgetall(name=self.name)

        response = await self.client.hmget(name=self.name, keys=keys)

        result = dict()
        for index, key in enumerate(keys):
            result[key] = response[index]

        return result

    def _hash_del_key(self, keys: list):
        """hash, Delete ``keys`` from hash ``name``

        have * need list         ([key, key, key])
            hdel(*[key, key, key])
        no   * need multiple key (key, key, key)
            hdel(key, key, key)
        """

        self.client.hdel(self.name, *keys)

    def _lis_push(self, values: list, is_right: bool = True):
        """list, Push ``values`` into the head or tail of the list ``name``, depend on is_right flag"""

        if is_right:
            return self.client.rpush(self.name, *values)
        else:
            return self.client.lpush(self.name, *values)

    def _list_left_range(self, start: int = 0, end: int = -1):
        """list, Return a slice of the list ``name`` between position ``start`` and ``end``"""

        return self.client.lrange(name=self.name, start=start, end=end)

    def _list_set(self, index: int, value: str):
        """list, Set element at ``index`` of list ``name`` to ``value``"""

        return self.client.lset(name=self.name, index=index, value=value)
