from fastapi.testclient import TestClient


def test_no_user(client: TestClient):
    # 存在しないユーザはエラーになること
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "User with the id 1 is not available"}

    # 存在しないユーザはログインできないこと
    response = client.post(
        "/login",
        data={
            "username": "testmail",
            "password": "testpassword",
        },
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid Credentials"}


def test_create_user(client: TestClient):
    # ユーザ作成ができること
    response = client.post(
        "/users/",
        json={
            "name": "testname",
            "email": "testmail",
            "password": "testpassword",
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        "name": "testname",
        "email": "testmail",
        "blogs": [],
    }

    # 作成したユーザ情報が取得できること
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "testname",
        "email": "testmail",
        "blogs": [],
    }

    # 作成したユーザでログインできること
    response = client.post(
        "/login",
        data={
            "username": "testmail",
            "password": "testpassword",
        },
    )
    assert response.status_code == 200
    tokens = response.json()
    assert "access_token" in tokens
    assert tokens["token_type"] == "bearer"
