from app.database.db import db


class User(db.Model):
    """User model."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    username = db.Column(
        db.String(50),
        unique=True,
        nullable=False,
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False,
    )

    password = db.Column(
        db.String(255),
        nullable=False,
    )

    def to_dict(self):
        """Return a JSON-serializable representation of the user."""

        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }