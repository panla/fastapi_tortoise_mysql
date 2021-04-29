import pytest
from httpx import AsyncClient

from apps import create_app
from tests.utils.tools import random_str


@pytest.mark.asyncio
async def test_root():
    app = create_app()

    brand = random_str(20)
    price = 20000

    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/api/v1/admin/cars", json={'brand': brand, 'price': price})

        print(response.json())
    assert response.status_code == 201
