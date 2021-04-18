from typing import Generator

import pytest

from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer

from apps import create_app


@pytest.fixture(scope='module')
def client() -> Generator:
    app = create_app()

    initializer(['apps.models.__init__'])
    with TestClient(app) as c:
        yield c

    finalizer()


@pytest.fixture(scope='module')
def event_loop(client: TestClient) -> Generator:
    yield client.task.get_loop()
