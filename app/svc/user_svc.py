"""Module contains the service layer for the user module."""
# -*- encoding: utf-8 -*-
from typing import Optional, Sequence

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
    res = await user_repo.create_user(username, password, email)
    return res


async def list_users(user_ids: list[int]) -> Sequence[Users]:
    """
    Retrieve a list of users.

    Returns:
        List[User]: A list of User objects representing the users.
    """
    res = await user_repo.list_users(user_ids)
    return res


async def login(username: str, password: str) -> Optional[Users]:
    """
    Find user and compare password for login

    Args:
        username (str):
        password (str):

    Returns:
        bool: Login status
    """
    res = await user_repo.get_user(user_repo.UserFlow(by_username=username))
    if not res:
        return None
    
    # compare password
    if res.password != password:
        raise ValueError("wrong password")
    return res
