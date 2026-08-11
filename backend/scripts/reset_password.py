import sys

from app import create_app
from app.database.db import db
from app.models.user import User
from app.utils.password import hash_password


def reset_password(email, new_password):
    app = create_app()

    with app.app_context():
        user = User.query.filter_by(email=email).first()

        if not user:
            print(f"User '{email}' not found.")
            return

        user.password = hash_password(new_password)

        db.session.commit()

        print(f"Password reset successfully for {email}.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python scripts/reset_password.py <email> <new_password>"
        )
        sys.exit(1)

    reset_password(
        sys.argv[1],
        sys.argv[2],
    )