from flask import jsonify
from werkzeug.exceptions import HTTPException

from app.utils.validators import ValidationError


def register_error_handlers(app):
    """Register global exception handlers."""

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return (
            jsonify(
                {
                    "error": "Validation Error",
                    "message": error.message,
                }
            ),
            400,
        )

    @app.errorhandler(404)
    def handle_not_found(error):
        return (
            jsonify(
                {
                    "error": "Not Found",
                    "message": "The requested resource was not found.",
                }
            ),
            404,
        )

    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        return (
            jsonify(
                {
                    "error": "Method Not Allowed",
                    "message": "HTTP method is not allowed for this endpoint.",
                }
            ),
            405,
        )

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return (
            jsonify(
                {
                    "error": error.name,
                    "message": error.description,
                }
            ),
            error.code,
        )

    @app.errorhandler(Exception)
    def handle_exception(error):
        app.logger.exception(error)

        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred.",
                }
            ),
            500,
        )
