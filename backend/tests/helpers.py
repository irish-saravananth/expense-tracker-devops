def register_user(client):
    """Register a test user."""

    return client.post(
        "/api/v1/auth/register",
        json={
            "username": "expenseuser",
            "email": "expense@example.com",
            "password": "Password123!",
        },
    )


def login_user(client):
    """Login the test user and return the JWT access token."""

    register_user(client)

    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "expense@example.com",
            "password": "Password123!",
        },
    )

    return response.get_json()["access_token"]


def auth_headers(client):
    """Return Authorization headers containing a valid JWT."""

    token = login_user(client)

    return {
        "Authorization": f"Bearer {token}"
    }