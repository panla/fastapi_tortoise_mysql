import asyncio

import pytest
from starlette.config import environ
from starlette.testclient import TestClient
from tortoise import Tortoise, generate_schema_for_client

import tortoise_conf_test

environ["CODE_ENV"] = "test"


@pytest.fixture(scope="session")
def loop():
    loop = asyncio.get_event_loop()
    return loop


@pytest.fixture(scope="session", autouse=True)
def client(loop, request):
    # 初始化tortoise-orm的连接，autouse 自动调用，启动pytest的时候会自动调用
    from apps import create_app

    loop.run_until_complete(Tortoise.init(config=tortoise_conf_test.TORTOISE_ORM, _create_db=True))
    # 创建数据库，创建一个临时数据库

    app = create_app()

    loop.run_until_complete(
        generate_schema_for_client(Tortoise.get_connection("default"), safe=True)
    )

    with TestClient(app) as client:
        yield client

    # 这里使用回调的方式，在左右测试完毕的时候会删除该数据库
    # 尝试删除所有数据库，在所有的数据操作完毕之后回调该方法删除数据库
    request.addfinalizer(lambda: loop.run_until_complete(Tortoise._drop_databases()))
