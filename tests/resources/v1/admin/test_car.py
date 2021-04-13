import random

from tests.utils.tools import random_str


def test_create_user(client):
    brand = random_str(19)
    data = {'brand': brand, 'price': random.randint(10000, 100000)}
    r = client.post("/api/v1/admin/cars", json=data)
    r.raise_for_status()
