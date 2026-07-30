def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "UP"
    assert data["service"] == "expense-tracker-api"
    assert data["version"] == "0.1.0"