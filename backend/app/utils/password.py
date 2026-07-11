import bcrypt


def hash_password(password: str) -> str:
    """Hash a plaintext password."""

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt(),
    )

    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a plaintext password."""

    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8"),
    )
