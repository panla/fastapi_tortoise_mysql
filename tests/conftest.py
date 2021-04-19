import asyncio

import pytest

from tortoise import Tortoise
from tortoise import generate_schema_for_client

from tortoise_conf_test import TORTOISE_ORM


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await Tortoise.init(config=TORTOISE_ORM, _create_db=True)

    # 创建数据库
    await generate_schema_for_client(Tortoise.get_connection("default"), safe=True)

    yield
    await Tortoise._drop_databases()
