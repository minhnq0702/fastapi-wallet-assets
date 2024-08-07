"""User repository module."""
# -*- encoding: utf-8 -*-
from app.models.users import Users
from app.repo import database


async def create_user(username: str, password: str) -> Users:
    """Create a new user

    Args:
        username (str): Username
        password (str): Password

    Returns:
        Users: User object
    """
    dbc = database.get_tx()
    db = await anext(dbc)
    user = Users(username=username, password=password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
