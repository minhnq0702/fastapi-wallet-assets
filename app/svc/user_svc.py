"""Module contains the service layer for the user module."""
# -*- coding: utf-8 -*-
import typing

from app.graphql.user import User
from app.repo import user_repo


async def create_user(username: str, password: str, email: str) -> User:
    """
    Create a new user.

    Args:
        username (str): Username of the user.
        password (str): Password of the user.
        email (str): Email of the user.

    Returns:
        User: A User object representing the user.
    """
    res = await user_repo.create_user(username='test', password='adsf')
    return res


async def get_users() -> typing.List[User]:
    """
    Retrieve a list of users.

    Returns:
        List[User]: A list of User objects representing the users.
    """
    await create_user('test', 'adsf', 'adsf')
    return [
        # User(username="minhnq", password="password1", email="minhnq@gmail.com"),
        # User(username="trangntt", password="password1", email="minhnq@gmail.com")
    ]
