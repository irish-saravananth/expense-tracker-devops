from app.database.db import db
from app.models.expense import Expense


class ExpenseService:
    """Service layer for expense operations."""

    @staticmethod
    def create_expense(
        user_id,
        title,
        description,
        amount,
        category,
        expense_date,
    ):
        """Create a new expense."""

        expense = Expense(
            user_id=user_id,
            title=title,
            description=description,
            amount=amount,
            category=category,
            expense_date=expense_date,
        )

        db.session.add(expense)
        db.session.commit()

        return expense

    @staticmethod
    def get_all_expenses(user_id):
        """Return all expenses for a user."""

        return (
            Expense.query.filter_by(user_id=user_id)
            .order_by(Expense.expense_date.desc())
            .all()
        )

    @staticmethod
    def get_expense(expense_id, user_id):
        """Return a single expense belonging to a user."""

        return Expense.query.filter_by(
            id=expense_id,
            user_id=user_id,
        ).first()

    @staticmethod
    def update_expense(expense, data):
        """Update an existing expense."""

        expense.title = data.get("title", expense.title)
        expense.description = data.get(
            "description",
            expense.description,
        )
        expense.amount = data.get("amount", expense.amount)
        expense.category = data.get(
            "category",
            expense.category,
        )
        expense.expense_date = data.get(
            "expense_date",
            expense.expense_date,
        )

        db.session.commit()

        return expense

    @staticmethod
    def delete_expense(expense):
        """Delete an expense."""

        db.session.delete(expense)
        db.session.commit()