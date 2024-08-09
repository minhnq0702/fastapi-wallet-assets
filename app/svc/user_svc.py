"""Module contains the service layer for the user module."""
# -*- coding: utf-8 -*-
import typing

from app.models.users import Users
from app.repo import user_repo


async def create_user(username: str, password: str, email: str) -> Users:
    """
    Create a new user.

    Args:
        username (str): Username of the user.
        password (str): Password of the user.
        email (str): Email of the user.

    Returns:
        User: A User object representing the user.
    """
    res = await user_repo.create_user(username=username, password=password, email=email)
    return res


async def get_users() -> typing.List[Users]:
    """
    Retrieve a list of users.

    Returns:
        List[User]: A list of User objects representing the users.
    """
    # await create_user('test', 'adsf', 'adsf')
    u1 = Users(id=1, username="minhnq", password="password1", email="minhnq@gmail.com")
    u2 = Users(id=2, username="trangntt", password="password1", email="minhnq@gmail.com")
    return [
        u1,
        u2,
    ]
