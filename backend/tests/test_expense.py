from tests.helpers import auth_headers


def test_create_expense(client):
    response = client.post(
        "/api/v1/expenses",
        headers=auth_headers(client),
        json={
            "title": "Laptop",
            "description": "Office laptop",
            "amount": 65000,
            "category": "Electronics",
            "expense_date": "2026-07-30",
        },
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Laptop"
    assert data["amount"] == 65000


def test_get_all_expenses(client):
    headers = auth_headers(client)

    client.post(
        "/api/v1/expenses",
        headers=headers,
        json={
            "title": "Coffee",
            "description": "",
            "amount": 150,
            "category": "Food",
            "expense_date": "2026-07-30",
        },
    )

    response = client.get(
        "/api/v1/expenses",
        headers=headers,
    )

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 1


def test_get_expense(client):
    headers = auth_headers(client)

    create = client.post(
        "/api/v1/expenses",
        headers=headers,
        json={
            "title": "Phone",
            "description": "",
            "amount": 50000,
            "category": "Electronics",
            "expense_date": "2026-07-30",
        },
    )

    expense_id = create.get_json()["id"]

    response = client.get(
        f"/api/v1/expenses/{expense_id}",
        headers=headers,
    )

    assert response.status_code == 200

    assert response.get_json()["title"] == "Phone"


def test_update_expense(client):
    headers = auth_headers(client)

    create = client.post(
        "/api/v1/expenses",
        headers=headers,
        json={
            "title": "Mouse",
            "description": "",
            "amount": 1000,
            "category": "Electronics",
            "expense_date": "2026-07-30",
        },
    )

    expense_id = create.get_json()["id"]

    response = client.put(
        f"/api/v1/expenses/{expense_id}",
        headers=headers,
        json={
            "amount": 1200
        },
    )

    assert response.status_code == 200

    assert response.get_json()["amount"] == 1200


def test_delete_expense(client):
    headers = auth_headers(client)

    create = client.post(
        "/api/v1/expenses",
        headers=headers,
        json={
            "title": "Keyboard",
            "description": "",
            "amount": 3000,
            "category": "Electronics",
            "expense_date": "2026-07-30",
        },
    )

    expense_id = create.get_json()["id"]

    response = client.delete(
        f"/api/v1/expenses/{expense_id}",
        headers=headers,
    )

    assert response.status_code == 200

    assert (
        response.get_json()["message"]
        == "Expense deleted successfully"
    )


def test_expense_requires_authentication(client):
    response = client.get("/api/v1/expenses")

    assert response.status_code == 401


def test_expense_not_found(client):
    response = client.get(
        "/api/v1/expenses/9999",
        headers=auth_headers(client),
    )

    assert response.status_code == 404