from flask import Flask

from app.config.settings import Config
from app.database.db import db, migrate

# Import models so Flask-Migrate can detect them
from app.models.user import User


def create_app():
    """Application factory."""

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.api.health import health_bp

    app.register_blueprint(health_bp)

    return app
