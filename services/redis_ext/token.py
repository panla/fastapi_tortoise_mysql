from .base import BaseRedis


class TokenRedis(BaseRedis):
    """full key: token:{phone}:{extend_model}:{extend_user_id}"""

    DB = 1
    PREFIX_KEY = 'token'
