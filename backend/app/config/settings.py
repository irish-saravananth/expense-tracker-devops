import os

from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Base application configuration.
    """

    SECRET_KEY = os.getenv("SECRET_KEY", "change-me")

    JWT_SECRET_KEY = os.getenv(
        "JWT_SECRET_KEY",
        "jwt-secret-change-me",
    )

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:

        SQLALCHEMY_DATABASE_URI = DATABASE_URL

    else:

        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_PORT = os.getenv("DB_PORT", "5432")
        DB_NAME = os.getenv("DB_NAME", "expense_tracker")
        DB_USER = os.getenv("DB_USER", "expense_user")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "expense_password")

        SQLALCHEMY_DATABASE_URI = (
            f"postgresql://{DB_USER}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
