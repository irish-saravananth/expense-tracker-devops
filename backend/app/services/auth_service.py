from app.database.db import db
from app.models.user import User
from app.utils.password import hash_password, verify_password


class AuthService:

    @staticmethod
    def register(username, email, password):

        existing = User.query.filter(
            (User.email == email) |
            (User.username == username)
        ).first()

        if existing:
            return None

        user = User(
            username=username,
            email=email,
            password=hash_password(password),
        )

        db.session.add(user)
        db.session.commit()

        return user

    @staticmethod
    def authenticate(email, password):

        user = User.query.filter_by(email=email).first()

        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user
