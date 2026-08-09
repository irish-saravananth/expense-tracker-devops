from flask import Flask
from flask_jwt_extended import JWTManager

from app.api.expense import expense_bp
from app.config.logging_config import configure_logging
from app.config.settings import Config
from app.database.db import db, migrate
from app.errors.handlers import register_error_handlers
from app.middleware.request_logger import (
    register_request_logger,
)

# Import models so Flask-Migrate detects them
from app.models.expense import Expense  # noqa: F401
from app.models.user import User  # noqa: F401

jwt = JWTManager()


def create_app(config_class=Config):
    """Application factory."""

    app = Flask(__name__)

    app.config.from_object(config_class)

    configure_logging(app)
    register_request_logger(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.api.auth import auth_bp
    from app.api.health import health_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(expense_bp)

    register_error_handlers(app)

    return app