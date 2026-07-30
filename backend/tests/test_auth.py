from app.models.user import User


def test_register_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "saravanan",
            "email": "saravanan@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["username"] == "saravanan"
    assert data["email"] == "saravanan@example.com"
    assert "id" in data


def test_duplicate_registration(client):
    payload = {
        "username": "duplicate",
        "email": "duplicate@example.com",
        "password": "Password123!",
    }

    client.post("/api/v1/auth/register", json=payload)

    response = client.post("/api/v1/auth/register", json=payload)

    assert response.status_code == 409

    assert response.get_json()["message"] == "User already exists"


def test_login_success(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "loginuser",
            "email": "login@example.com",
            "password": "Password123!",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "login@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "access_token" in data


def test_login_invalid_password(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "wrongpass",
            "email": "wrong@example.com",
            "password": "Password123!",
        },
    )

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "wrong@example.com",
            "password": "WrongPassword",
        },
    )

    assert response.status_code == 401

    assert response.get_json()["message"] == "Invalid credentials"


def test_login_unknown_user(client):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "nouser@example.com",
            "password": "Password123!",
        },
    )

    assert response.status_code == 401

    assert response.get_json()["message"] == "Invalid credentials"


def test_me_endpoint(client):
    client.post(
        "/api/v1/auth/register",
        json={
            "username": "jwtuser",
            "email": "jwt@example.com",
            "password": "Password123!",
        },
    )

    login = client.post(
        "/api/v1/auth/login",
        json={
            "email": "jwt@example.com",
            "password": "Password123!",
        },
    )

    token = login.get_json()["access_token"]

    response = client.get(
        "/api/v1/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["username"] == "jwtuser"
    assert data["email"] == "jwt@example.com"


def test_me_without_token(client):
    response = client.get("/api/v1/auth/me")

    assert response.status_code == 401