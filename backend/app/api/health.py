from flask import Blueprint, jsonify

health_bp = Blueprint(
    "health",
    __name__,
    url_prefix="/api/v1",
)


@health_bp.route("/health", methods=["GET"])
def health():
    return (
        jsonify(
            {
                "status": "UP",
                "service": "expense-tracker-api",
                "version": "0.1.0",
            }
        ),
        200,
    )