from .base import RedisClientBase, ResourceLock


class SMSCodeRedis(RedisClientBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'


class OrderLock(ResourceLock):
    """full key: recource_lock:orders:{key}"""

    DB = 2
    LOCK_PREFIX_KEY = 'orders:'
    _timeout = 3600

    def __init__(self, key) -> None:
        super().__init__(key)
        self.key = f'{self.PREFIX_KEY}{self.LOCK_PREFIX_KEY}{key}'
