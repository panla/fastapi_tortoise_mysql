from .base import RedisClientBase, ResourceLock


class SMSCodeRedis(RedisClientBase):
    DB = 1
    PREFIX_KEY = 'sms_code:'


class OrderLock(ResourceLock):
    DB = 2
    PREFIX_KEY = 'order_lock:'
    _timeout = 3600

    def __init__(self, key, order_id) -> None:
        super().__init__(key)
        self.key = f'{self.PREFIX_KEY}{key}:{order_id}'
