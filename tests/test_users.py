from fastapi.testclient import TestClient


def test_create_user_returns_created_user(client: TestClient) -> None:
    response = client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "billy"
    assert data["email"] == "billy@example.com"
    assert "hashed_password" not in data
    assert "password" not in data


def test_create_user_with_existing_username_returns_400(client: TestClient) -> None:
    client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "different@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "User with that username already exists."
    }


def test_create_user_with_existing_email_returns_400(client: TestClient) -> None:
    client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/users/",
        json={
            "username": "different",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "User with that email already exists."
    }


def test_create_user_with_existing_username_and_email_returns_400(
    client: TestClient,
) -> None:
    client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/users/",
        json={
            "username": "billy",
            "email": "billy@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 400
    assert response.json() == {
        "detail": "User with both that username and email already exists."
    }