from .base import BaseRedisClient


class TokenRedis(BaseRedisClient):
    """full key: token:{phone}:{extend_model}:{extend_user_id}"""

    DB = 1
    PREFIX_KEY = 'token'
