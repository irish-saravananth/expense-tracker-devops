from datetime import datetime

from app.database.db import db


class Expense(db.Model):
    """Expense model."""

    __tablename__ = "expenses"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    title = db.Column(
        db.String(100),
        nullable=False,
    )

    description = db.Column(
        db.String(255),
        nullable=True,
    )

    amount = db.Column(
        db.Numeric(10, 2),
        nullable=False,
    )

    category = db.Column(
        db.String(50),
        nullable=False,
    )

    expense_date = db.Column(
        db.Date,
        nullable=False,
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False,
    )

    user = db.relationship(
        "User",
        back_populates="expenses",
    )

    def to_dict(self):
        """Serialize expense."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "amount": float(self.amount),
            "category": self.category,
            "expense_date": self.expense_date.isoformat(),
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }