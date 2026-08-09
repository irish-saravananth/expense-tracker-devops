from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.services.expense_service import ExpenseService
from app.utils.validators import validate_expense

expense_bp = Blueprint(
    "expense",
    __name__,
    url_prefix="/api/v1/expenses",
)


@expense_bp.route("", methods=["POST"])
@jwt_required()
def create_expense():
    """Create a new expense."""

    user_id = int(get_jwt_identity())
    data = request.get_json()

    validate_expense(data)

    expense = ExpenseService.create_expense(
        user_id=user_id,
        title=data["title"],
        description=data.get("description"),
        amount=data["amount"],
        category=data["category"],
        expense_date=datetime.strptime(
            data["expense_date"],
            "%Y-%m-%d",
        ).date(),
    )

    return jsonify(expense.to_dict()), 201


@expense_bp.route("", methods=["GET"])
@jwt_required()
def get_all_expenses():
    """Return all expenses for the authenticated user."""

    user_id = int(get_jwt_identity())

    expenses = ExpenseService.get_all_expenses(user_id)

    return jsonify(
        [expense.to_dict() for expense in expenses]
    ), 200


@expense_bp.route("/<int:expense_id>", methods=["GET"])
@jwt_required()
def get_expense(expense_id):
    """Return a specific expense."""

    user_id = int(get_jwt_identity())

    expense = ExpenseService.get_expense(
        expense_id,
        user_id,
    )

    if not expense:
        return (
            jsonify(
                {
                    "message": "Expense not found",
                }
            ),
            404,
        )

    return jsonify(expense.to_dict()), 200


@expense_bp.route("/<int:expense_id>", methods=["PUT"])
@jwt_required()
def update_expense(expense_id):
    """Update an expense."""

    user_id = int(get_jwt_identity())

    expense = ExpenseService.get_expense(
        expense_id,
        user_id,
    )

    if not expense:
        return (
            jsonify(
                {
                    "message": "Expense not found",
                }
            ),
            404,
        )

    data = request.get_json()

    # Validate only the fields supplied by the client
    merged_data = {
        "title": data.get("title", expense.title),
        "description": data.get(
            "description",
            expense.description,
        ),
        "amount": data.get("amount", expense.amount),
        "category": data.get(
            "category",
            expense.category,
        ),
        "expense_date": data.get(
            "expense_date",
            expense.expense_date.strftime("%Y-%m-%d"),
        ),
    }

    validate_expense(merged_data)

    if "expense_date" in data:
        data["expense_date"] = datetime.strptime(
            data["expense_date"],
            "%Y-%m-%d",
        ).date()

    expense = ExpenseService.update_expense(
        expense,
        data,
    )

    return jsonify(expense.to_dict()), 200


@expense_bp.route("/<int:expense_id>", methods=["DELETE"])
@jwt_required()
def delete_expense(expense_id):
    """Delete an expense."""

    user_id = int(get_jwt_identity())

    expense = ExpenseService.get_expense(
        expense_id,
        user_id,
    )

    if not expense:
        return (
            jsonify(
                {
                    "message": "Expense not found",
                }
            ),
            404,
        )

    ExpenseService.delete_expense(expense)

    return (
        jsonify(
            {
                "message": "Expense deleted successfully",
            }
        ),
        200,
    )