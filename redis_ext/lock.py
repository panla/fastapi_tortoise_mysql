import time
from typing import Union, Tuple

from .base import BaseRedis


class BaseLockRedis(BaseRedis):
    """full key: Lock:{key}"""

    DB = 2
    PREFIX_KEY = 'Lock'
    TIMEOUT = 3600

    async def get_lock(self) -> Tuple[bool, Union[str, None]]:
        """get the lock"""

        current_time = time.time()
        current_value = current_time + self.TIMEOUT

        lock = await self.set(value=current_value, ex=self.TIMEOUT, nx=True)
        if lock:
            # origin is not exists now set it OK
            return True, str(current_value)

        # it had exists, get_old_value
        old_lock = await self.get()

        if old_lock and current_time > float(old_lock):
            # had expired
            # set new and get old
            old_value = await self.set(value=current_value, ex=self.TIMEOUT, get=True)
            if not old_value or old_lock == old_value:
                return True, str(current_value)
            return False, None
        return False, None


class OrderLockRedis(BaseLockRedis):
    """full key: orderLock:{key}"""

    DB = 2
    PREFIX_KEY = 'orderLock'
    TIMEOUT = 3600
