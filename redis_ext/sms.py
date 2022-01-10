from .base import BaseRedisClient


class SMSCodeRedis(BaseRedisClient):
    """full key: sms_code:{key}"""

    DB = 1
    PREFIX_KEY = 'sms_code'

    def __init__(self, key) -> None:
        super().__init__(key)
        self.key = f'{self.PREFIX_KEY}:{key}'
