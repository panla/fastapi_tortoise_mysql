from .base import BaseRedisClient


class TokenRedis(BaseRedisClient):
    """full key: token:{user_id}:{extend_model}:{extend_user_id}"""

    DB = 1
    PREFIX_KEY = 'token'

    def __init__(self, user_id, extend_model, extend_user_id) -> None:
        super().__init__()
        self.key = f'{self.PREFIX_KEY}:{user_id}:{extend_model}:{extend_user_id}'

    def set_login_info(self, mapping: dict):
        """set token

        mapping: key: value
            {
                "login_at": float,
                "token_expired": float,
                "extend_user_id": int
            }
        """

        return self.client.hmset(self.key, mapping=mapping)

    def get_login_info(self, keys: list):
        """get token

        keys: [key]
        """

        return self.client.hmget(self.key, keys=keys)
