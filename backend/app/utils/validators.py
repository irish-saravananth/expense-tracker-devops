import re
from datetime import datetime


class ValidationError(Exception):
    """Custom exception raised for validation errors."""

    def __init__(self, message):
        self.message = message
        super().__init__(message)


EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def validate_email(email):
    if not email:
        raise ValidationError("Email is required.")

    if not re.match(EMAIL_REGEX, email):
        raise ValidationError("Invalid email address.")


def validate_password(password):
    if not password:
        raise ValidationError("Password is required.")

    if len(password) < 8:
        raise ValidationError(
            "Password must be at least 8 characters long."
        )

    if not re.search(r"[A-Z]", password):
        raise ValidationError(
            "Password must contain at least one uppercase letter."
        )

    if not re.search(r"[a-z]", password):
        raise ValidationError(
            "Password must contain at least one lowercase letter."
        )

    if not re.search(r"\d", password):
        raise ValidationError(
            "Password must contain at least one number."
        )


def validate_register(data):
    if not data:
        raise ValidationError("Request body is required.")

    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not name:
        raise ValidationError("Name is required.")

    validate_email(email)
    validate_password(password)


def validate_login(data):
    if not data:
        raise ValidationError("Request body is required.")

    email = data.get("email", "").strip()
    password = data.get("password", "")

    validate_email(email)

    if not password:
        raise ValidationError("Password is required.")


def validate_expense(data):
    if not data:
        raise ValidationError("Request body is required.")

    title = data.get("title", "").strip()

    if not title:
        raise ValidationError("Title is required.")

    if len(title) > 100:
        raise ValidationError(
            "Title cannot exceed 100 characters."
        )

    amount = data.get("amount")

    if amount is None:
        raise ValidationError("Amount is required.")

    try:
        amount = float(amount)
    except (ValueError, TypeError):
        raise ValidationError(
            "Amount must be a valid number."
        )

    if amount <= 0:
        raise ValidationError(
            "Amount must be greater than zero."
        )

    category = data.get("category", "").strip()

    if not category:
        raise ValidationError("Category is required.")

    expense_date = data.get("expense_date")

    if not expense_date:
        raise ValidationError(
            "Expense date is required."
        )

    try:
        datetime.strptime(expense_date, "%Y-%m-%d")
    except ValueError:
        raise ValidationError(
            "Expense date must be in YYYY-MM-DD format."
        )

    description = data.get("description", "")

    if len(description) > 500:
        raise ValidationError(
            "Description cannot exceed 500 characters."
        )
