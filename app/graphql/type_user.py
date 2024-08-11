"""User GraphQL schema."""
# -*- coding: utf-8 -*-

import typing

import strawberry

from app.graphql.utils import model_to_strawberry
from app.models.users import Users
from app.svc.user_svc import create_user as svc_create_user
from app.svc.user_svc import get_users as svc_get_user


@strawberry.experimental.pydantic.type(model=Users)
class UserType:
    """User schema."""
    id: typing.Optional[int]
    username: str
    password: str
    email: str


@strawberry.input
class UserCreateType:
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
    return [model_to_strawberry(u, UserType) for u in res]


async def create_user(user: UserCreateType) -> UserType:
    """Create a new user

    Args:
        user (CreateUserType): User object

    Returns:
        UserType: User object
    """
    assert len(user.username) > 0, "username must not be empty"
    assert len(user.password) >= 8, "password must more or equal 8 characters"
    res = await svc_create_user(user.username, user.password, user.email)
    return model_to_strawberry(res, UserType)
