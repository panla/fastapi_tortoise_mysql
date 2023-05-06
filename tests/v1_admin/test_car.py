import os

from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED


def test_read_book_first(client: TestClient):
    url = '/api/admin/cars/1'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)
    assert response.status_code == HTTP_200_OK


def test_update_car(client: TestClient):
    url = '/api/admin/cars/1'
    params = {
        'price': 200
    }
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.patch(url, headers=headers, json=params)
    assert response.status_code == HTTP_201_CREATED


def test_read_car_two(client: TestClient):
    url = '/api/admin/cars/1'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)
    assert response.status_code == HTTP_200_OK
    # assert response.status_code == 201


def test_cars_count(client: TestClient):
    url = '/api/admin/cars'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)

    assert response.status_code == HTTP_200_OK
    assert response.json().get('data').get('total') == 5
