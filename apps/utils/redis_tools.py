from aioredis import create_redis_pool

import config


async def register_redis():
    """redis 连接池"""

    redis_uri = f"redis://:@{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}?encoding=utf-8"
    return await create_redis_pool(redis_uri)
