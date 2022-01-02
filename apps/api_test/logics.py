from extensions import logger
from redis_ext import TokenRedis


class RedisTestResolver:

    @classmethod
    async def test_set(cls):
        await cls._test_token_redis()

    @staticmethod
    async def _test_token_redis():
        extend_model = 'AdminUser'
        user_id = 1
        extend_user_id = 1

        obj = TokenRedis(str(user_id), extend_model, extend_user_id)
        rt_0 = await obj.set_login_info({'name': '123', 'age': 14})

        rt_1 = await obj.get_login_info(['name'])
        rt_2 = await obj.get_login_info(['name', 'age'])

        logger.info(rt_0)
        logger.info(rt_1)
        logger.info(rt_2)
