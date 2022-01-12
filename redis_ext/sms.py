from .base import BaseRedisClient


class SMSCodeRedis(BaseRedisClient):
    """full key: sms_code:{key}"""

    DB = 1
    PREFIX_KEY = 'sms_code'
