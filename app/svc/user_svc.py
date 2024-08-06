"""Module contains the service layer for the user module."""
# -*- coding: utf-8 -*-
import typing

from app.graphql.user import User


async def get_users() -> typing.List[User]:
    """
    Retrieve a list of users.

    Returns:
        List[User]: A list of User objects representing the users.
    """
    return [
        User(username="minhnq", password="password1", email="minhnq@gmail.com"),
        User(username="trangntt", password="password1", email="minhnq@gmail.com")
    ]
