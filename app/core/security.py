# -*- encoding: utf-8 -*-
import bcrypt


def encrypt(password) -> str:
    """Encrypt password

    Args:
        password (str): _description_
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password=password.encode(), salt=salt)
    return hashed.decode()


def verify_password(plain_password: str, hash_password: str):
    """Verify hashed password and plain text password

    Args:
        plain_password (str): Plain text password
        hash_password (str): Hashed password

    Returns:
        bool: password is matched or not
    """
    return bcrypt.checkpw(plain_password.encode(), hash_password.encode())


if __name__ == "__main__":
    PASSWORD = "testpassword"
    hashed_password = encrypt(PASSWORD)
    print(verify_password(PASSWORD, hashed_password))
