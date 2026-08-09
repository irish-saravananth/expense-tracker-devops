import pytest

from app.utils.validators import (
    ValidationError,
    validate_email,
    validate_expense,
    validate_login,
    validate_password,
    validate_register,
)


# -----------------------------
# Email Validation
# -----------------------------

def test_validate_email_success():
    validate_email("user@example.com")


def test_validate_email_missing():
    with pytest.raises(ValidationError):
        validate_email("")


def test_validate_email_invalid():
    with pytest.raises(ValidationError):
        validate_email("invalid-email")


# -----------------------------
# Password Validation
# -----------------------------

def test_validate_password_success():
    validate_password("Password123")


def test_validate_password_too_short():
    with pytest.raises(ValidationError):
        validate_password("Pass1")


def test_validate_password_missing_uppercase():
    with pytest.raises(ValidationError):
        validate_password("password123")


def test_validate_password_missing_lowercase():
    with pytest.raises(ValidationError):
        validate_password("PASSWORD123")


def test_validate_password_missing_number():
    with pytest.raises(ValidationError):
        validate_password("Password")


# -----------------------------
# Register Validation
# -----------------------------

def test_validate_register_missing_body():
    with pytest.raises(ValidationError):
        validate_register(None)


def test_validate_register_missing_name():
    with pytest.raises(ValidationError):
        validate_register(
            {
                "name": "",
                "email": "user@example.com",
                "password": "Password123",
            }
        )


# -----------------------------
# Login Validation
# -----------------------------

def test_validate_login_missing_body():
    with pytest.raises(ValidationError):
        validate_login(None)


def test_validate_login_missing_password():
    with pytest.raises(ValidationError):
        validate_login(
            {
                "email": "user@example.com",
                "password": "",
            }
        )


# -----------------------------
# Expense Validation
# -----------------------------

def test_validate_expense_success():
    validate_expense(
        {
            "title": "Laptop",
            "description": "Office",
            "amount": 50000,
            "category": "Electronics",
            "expense_date": "2026-07-30",
        }
    )


def test_validate_expense_missing_title():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "",
                "amount": 100,
                "category": "Food",
                "expense_date": "2026-07-30",
            }
        )


def test_validate_expense_negative_amount():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "Coffee",
                "amount": -10,
                "category": "Food",
                "expense_date": "2026-07-30",
            }
        )


def test_validate_expense_invalid_amount():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "Coffee",
                "amount": "abc",
                "category": "Food",
                "expense_date": "2026-07-30",
            }
        )


def test_validate_expense_missing_category():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "Coffee",
                "amount": 100,
                "category": "",
                "expense_date": "2026-07-30",
            }
        )


def test_validate_expense_invalid_date():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "Coffee",
                "amount": 100,
                "category": "Food",
                "expense_date": "30-07-2026",
            }
        )


def test_validate_expense_long_description():
    with pytest.raises(ValidationError):
        validate_expense(
            {
                "title": "Coffee",
                "description": "A" * 501,
                "amount": 100,
                "category": "Food",
                "expense_date": "2026-07-30",
            }
        )