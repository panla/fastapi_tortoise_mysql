import asyncio

from fastapi.testclient import TestClient

from tests.utils.tools import random_str


def test_create_car(client: TestClient, event_loop: asyncio.AbstractEventLoop):
    brand = random_str(20)
    price = 10000

    response = client.post('/api/v1/admin/cars', json={'brand': brand, 'price': price})
    assert response.status_code == 201, response.json()
