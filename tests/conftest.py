__all__ = [
    'client', 'event_loop'
]

"""
need pip install pytest requests
"""

import sys
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from tortoise import run_async

from tests import BASE_DIR
from .pre_post import generate_db, delete_database

sys.path.append(BASE_DIR)

from apps import create_app


# @pytest.fixture(scope="function", autouse=True)
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
# @pytest.fixture(scope="package", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def client() -> Generator:
    try:
        run_async(generate_db())
        with TestClient(create_app()) as c:
            yield c
    finally:
        run_async(delete_database())


@pytest.fixture(scope="session", autouse=True)
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()
