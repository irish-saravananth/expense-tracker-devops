import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)s | "
    "%(name)s | "
    "%(message)s"
)


def configure_logging(app):
    """Configure application logging."""

    formatter = logging.Formatter(LOG_FORMAT)

    app_handler = RotatingFileHandler(
        LOG_DIR / "application.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)

    error_handler = RotatingFileHandler(
        LOG_DIR / "error.log",
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))
    console_handler.setFormatter(formatter)

    app.logger.handlers.clear()

    app.logger.addHandler(console_handler)
    app.logger.addHandler(app_handler)
    app.logger.addHandler(error_handler)

    app.logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    app.logger.info("Expense Tracker API logging initialized.")