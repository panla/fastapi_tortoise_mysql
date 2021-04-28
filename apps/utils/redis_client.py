from aioredis import create_redis_pool

import config

redis_client = None


async def redis_pool():
    """redis 连接池"""

    global redis_client
    redis_uri = f"redis://:@{config.REDIS_HOST}:{config.REDIS_PORT}/{config.REDIS_DB}?encoding=utf-8"

    pool = redis_client or await create_redis_pool(redis_uri, password=config.REDIS_PASSWD or None)
    redis_client = pool
    return pool
