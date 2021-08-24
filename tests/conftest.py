__all__ = [
    'client', 'event_loop'
]

"""
need pip install pytest requests
"""

from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise import run_async

from tests import create_app
from tests.pre_post import create_database, delete_database
from tests.utils import admin_user_test_token


# @pytest.fixture(scope="function", autouse=True)
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
# @pytest.fixture(scope="package", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def client() -> Generator:
    try:
        run_async(create_database())
        with TestClient(create_app()) as test_client:
            yield test_client
    finally:
        run_async(delete_database())


@pytest.fixture(scope="session", autouse=True)
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()


@pytest.fixture(scope="session", autouse=True)
def admin_user_token(client: TestClient):
    event_loop = client.task.get_loop()
    yield event_loop.run_until_complete(admin_user_test_token())
