from flask import Flask
from flask_jwt_extended import JWTManager

from app.config.settings import Config
from app.config.logging_config import configure_logging
from app.middleware.request_logger import register_request_logger
from app.database.db import db, migrate
from app.api.expense import expense_bp
from app.errors.handlers import register_error_handlers

# Import models so Flask-Migrate detects them
from app.models.user import User
from app.models.expense import Expense

jwt = JWTManager()


def create_app():
    """Application factory."""

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Configure logging
    configure_logging(app)
    register_request_logger(app)


    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from app.api.health import health_bp
    from app.api.auth import auth_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(expense_bp)

    # Register global error handlers
    register_error_handlers(app)

    return app