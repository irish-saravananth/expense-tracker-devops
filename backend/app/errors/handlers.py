from http import HTTPStatus

from flask import jsonify, g
from werkzeug.exceptions import HTTPException

from app.utils.validators import ValidationError


def register_error_handlers(app):
    """Register global error handlers."""

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        app.logger.warning(
            "RequestID=%s | Validation Error | %s",
            getattr(g, "request_id", "N/A"),
            str(error),
        )

        return (
            jsonify(
                {
                    "error": "Validation Error",
                    "message": str(error),
                }
            ),
            HTTPStatus.BAD_REQUEST,
        )

    @app.errorhandler(404)
    def handle_not_found(error):
        app.logger.warning(
            "RequestID=%s | Resource not found | %s",
            getattr(g, "request_id", "N/A"),
            error,
        )

        return (
            jsonify(
                {
                    "error": "Not Found",
                    "message": "Requested resource was not found.",
                }
            ),
            HTTPStatus.NOT_FOUND,
        )

    @app.errorhandler(405)
    def handle_method_not_allowed(error):
        app.logger.warning(
            "RequestID=%s | Method not allowed | %s",
            getattr(g, "request_id", "N/A"),
            error,
        )

        return (
            jsonify(
                {
                    "error": "Method Not Allowed",
                    "message": "HTTP method is not allowed.",
                }
            ),
            HTTPStatus.METHOD_NOT_ALLOWED,
        )

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        app.logger.warning(
            "RequestID=%s | HTTP Exception | %s",
            getattr(g, "request_id", "N/A"),
            error.description,
        )

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
    def handle_unexpected_exception(error):
        app.logger.exception(
            "RequestID=%s | Unhandled Exception",
            getattr(g, "request_id", "N/A"),
        )

        return (
            jsonify(
                {
                    "error": "Internal Server Error",
                    "message": "An unexpected error occurred.",
                }
            ),
            HTTPStatus.INTERNAL_SERVER_ERROR,
        )