"""User GraphQL schema."""
# -*- coding: utf-8 -*-

import typing

import strawberry

from app.svc.user_svc import create_user as svc_create_user


@strawberry.type
class UserType:
    """User object schema."""
    id: typing.Optional[int]
    username: str
    password: str
    email: str


@strawberry.input
class CreateUserType(UserType):
    """User object schema."""


async def list_user() -> typing.List[UserType]:
    """List users

    Returns:
        typing.List[UserType]: list of users
    """
    return []


async def create_user(user: CreateUserType) -> UserType:
    """Create a new user

    Args:
        user (CreateUserType): User object

    Returns:
        UserType: User object
    """
    res = await svc_create_user(user.username, user.password, user.email)
    return UserType(id=res.id, username=res.username, password=res.password, email=res.email)
