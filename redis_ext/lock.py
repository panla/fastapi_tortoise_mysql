import time
from typing import Union, Tuple

from .base import BaseRedisClient


class BaseResourceLock(BaseRedisClient):
    """full key: resource_lock:{key}"""

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


class OrderLock(BaseResourceLock):
    """full key: recource_lock:orders:{key}"""

    DB = 2
    LOCK_PREFIX_KEY = 'orders:'
    _timeout = 3600

    def __init__(self, key) -> None:
        super().__init__(key)
        self.key = f'{self.PREFIX_KEY}{self.LOCK_PREFIX_KEY}{key}'
