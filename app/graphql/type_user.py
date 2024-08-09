"""User GraphQL schema."""
# -*- coding: utf-8 -*-

import typing

import strawberry

from app.svc.user_svc import create_user as svc_create_user
from app.svc.user_svc import get_users as svc_get_user


@strawberry.type
class UserType:
    """User schema."""
    id: typing.Optional[int]
    username: str
    password: str
    email: str


@strawberry.input
class CreateUserType:
    """Create user object."""
    username: str
    password: str
    email: str


async def list_user(user_ids: typing.Union[typing.List[int], None] = None) -> typing.List[UserType]:
    """List users

    Returns:
        typing.List[UserType]: list of users
    """
    res = await svc_get_user(user_ids=user_ids or [])

    return [UserType(id=u.id, username=u.username, password=u.password, email=u.email) for u in res]


async def create_user(user: CreateUserType) -> UserType:
    """Create a new user

    Args:
        user (CreateUserType): User object

    Returns:
        UserType: User object
    """
    res = await svc_create_user(user.username, user.password, user.email)
    return UserType(id=res.id, username=res.username, password=res.password, email=res.email)
