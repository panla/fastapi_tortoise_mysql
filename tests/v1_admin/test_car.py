from fastapi.testclient import TestClient


def test_read_book_first(admin_user_token: str, client: TestClient):

    headers = {
        'X-TOKEN': admin_user_token
    }

    response = client.get('/api/v1/admin/cars/1', headers=headers)
    assert response.status_code == 200


def test_update_book(admin_user_token: str, client: TestClient):

    params = {
        'price': 200
    }
    headers = {
        'X-TOKEN': admin_user_token
    }

    response = client.patch('/api/v1/admin/cars/1', headers=headers, json=params)
    assert response.status_code == 201


def test_read_cup_two(admin_user_token: str, client: TestClient):

    headers = {
        'X-TOKEN': admin_user_token
    }

    response = client.get("/api/v1/admin/cars/1", headers=headers)
    assert response.status_code == 200
    # assert response.status_code == 201


def test_cars_count(admin_user_token: str, client: TestClient):
    headers = {
        'X-TOKEN': admin_user_token
    }

    response = client.get("/api/v1/admin/cars", headers=headers)

    assert response.status_code == 200
    assert response.json().get('data').get('total') == 5
