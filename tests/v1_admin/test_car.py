import asyncio

from fastapi.testclient import TestClient

from tests.utils import admin_user_test_token


def test_read_book(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    token = event_loop.run_until_complete(admin_user_test_token())

    headers = {
        'X-TOKEN': token
    }

    response = client.get('/api/v1/admin/cars/1', headers=headers)
    print(response.json())
    assert response.status_code == 200


def test_update_book(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    token = event_loop.run_until_complete(admin_user_test_token())

    params = {
        'price': 200
    }
    headers = {
        'X-TOKEN': token
    }

    response = client.patch('/api/v1/admin/cars/1', headers=headers, json=params)
    print(response.json())
    assert response.status_code == 201


def test_read_cup2(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    """测试不同的 pytest.fixture(scope="") 造成的不同测试之间的影响"""
    token = event_loop.run_until_complete(admin_user_test_token())

    headers = {
        'X-TOKEN': token
    }

    response = client.get("/api/v1/admin/cars/1", headers=headers)
    print(response.json())
    assert response.status_code == 200
