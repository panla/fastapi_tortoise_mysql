
"""
need pip install pytest requests
"""
__all__ = [
    'client'
]

from typing import Generator

import pytest
from tortoise import run_async
from fastapi.testclient import TestClient

from tests import create_app
from tests.pre_write_data import create_database, delete_database
from tests.token import generate_token


# @pytest.fixture(scope="function", autouse=True)
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
# @pytest.fixture(scope="package", autouse=True)
@pytest.fixture(scope="session", autouse=True)
def client() -> Generator:
    try:
        # create db and create table and create data
        run_async(create_database())

        # set token into environ
        run_async(generate_token())
        with TestClient(create_app()) as test_client:
            yield test_client
    finally:
        # drop db
        run_async(delete_database())
