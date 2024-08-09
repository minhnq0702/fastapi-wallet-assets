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


async def get_users(user_ids: list[int]) -> typing.List[Users]:
    """
    Retrieve a list of users.

    Returns:
        List[User]: A list of User objects representing the users.
    """
    res = await user_repo.get_users(user_ids)
    return res
