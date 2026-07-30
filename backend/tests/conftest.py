import pytest

from app import create_app
from app.config.settings import TestingConfig
from app.database.db import db


@pytest.fixture(scope="session")
def app():
    """Create the Flask application for testing."""

    app = create_app(TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture(autouse=True)
def database(app):
    """Create a clean database for every test."""

    with app.app_context():
        db.drop_all()
        db.create_all()

        yield

        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    """Flask test client."""

    return app.test_client()


@pytest.fixture()
def runner(app):
    """Flask CLI runner."""

    return app.test_cli_runner()