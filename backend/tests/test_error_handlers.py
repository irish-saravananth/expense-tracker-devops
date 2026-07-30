from flask import Blueprint

from app.utils.validators import ValidationError


def test_404_not_found(client):
    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404

    data = response.get_json()

    assert data["error"] == "Not Found"
    assert data["message"] == "Requested resource was not found."


def test_405_method_not_allowed(client):
    response = client.post("/api/v1/health")

    assert response.status_code == 405

    data = response.get_json()

    assert data["error"] == "Method Not Allowed"
    assert data["message"] == "HTTP method is not allowed."


def test_validation_error_handler(client):
    response = client.post(
        "/api/v1/auth/register",
        json={},
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Validation Error"


def test_internal_server_error_handler(app, client):
    test_bp = Blueprint("test_errors", __name__)

    @test_bp.route("/api/v1/test-error")
    def raise_error():
        raise RuntimeError("Boom!")

    # Register only once
    if "test_errors" not in app.blueprints:
        app.register_blueprint(test_bp)

    response = client.get("/api/v1/test-error")

    assert response.status_code == 500

    data = response.get_json()

    assert data["error"] == "Internal Server Error"
    assert data["message"] == "An unexpected error occurred."