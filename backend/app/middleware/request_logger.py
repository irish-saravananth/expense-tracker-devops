import time
import uuid

from flask import g, request
from flask_jwt_extended import (
    get_jwt_identity,
    verify_jwt_in_request,
)


def register_request_logger(app):
    """Register request logging middleware."""

    @app.before_request
    def before_request():
        g.start_time = time.time()

        # Unique request ID for tracing
        g.request_id = str(uuid.uuid4())[:8]

    @app.after_request
    def after_request(response):
        duration = (time.time() - g.start_time) * 1000

        user_id = "Anonymous"

        try:
            verify_jwt_in_request(optional=True)
            identity = get_jwt_identity()

            if identity:
                user_id = identity

        except Exception:
            pass

        app.logger.info(
            (
                "RequestID=%s | "
                "Method=%s | "
                "Path=%s | "
                "Status=%s | "
                "Duration=%.2f ms | "
                "UserID=%s | "
                "IP=%s"
            ),
            g.request_id,
            request.method,
            request.path,
            response.status_code,
            duration,
            user_id,
            request.remote_addr,
        )

        return response