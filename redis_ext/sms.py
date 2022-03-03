from .base import BaseRedis


class SMSCodeRedis(BaseRedis):
    """full key: sms_code:{key}"""

    DB = 1
    PREFIX_KEY = 'sms_code'
