from flask import Flask
from flask_jwt_extended import JWTManager

from app.config.settings import Config
from app.database.db import db, migrate
from app.api.expense import expense_bp

# Import models so Flask-Migrate detects them
from app.models.user import User
from app.models.expense import Expense

jwt = JWTManager()


def create_app():
    """Application factory."""

    app = Flask(__name__)

    app.config.from_object(Config)

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

    return app