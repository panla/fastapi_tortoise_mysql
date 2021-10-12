import os

from fastapi.testclient import TestClient


def test_read_book_first(client: TestClient):

    url = '/api/v1/admin/cars/1'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)
    assert response.status_code == 200


def test_update_book(client: TestClient):

    url = '/api/v1/admin/cars/1'
    params = {
        'price': 200
    }
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.patch(url, headers=headers, json=params)
    assert response.status_code == 201


def test_read_cup_two(client: TestClient):

    url = '/api/v1/admin/cars/1'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)
    assert response.status_code == 200
    # assert response.status_code == 201


def test_cars_count(client: TestClient):

    url = '/api/v1/admin/cars'
    headers = {
        'X-TOKEN': os.environ.get('AdminUserTestToken')
    }

    response = client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json().get('data').get('total') == 5
