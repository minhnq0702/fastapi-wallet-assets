"""User GraphQL schema."""
# -*- coding: utf-8 -*-

import typing

import strawberry

from app.models.users import Users
from app.svc import user_svc


@strawberry.experimental.pydantic.type(model=Users, name='User')
class UserType:
    """User type."""
    id: typing.Optional[int]
    username: strawberry.auto
    password: strawberry.auto
    email: strawberry.auto
    created_date: strawberry.auto
    updated_date: strawberry.auto


@strawberry.input
class UserCreateInput:
    """Create user type."""
    username: str
    password: str
    email: str


async def list_users(user_ids: typing.Union[typing.List[int], None] = None) -> typing.List[UserType]:
    """List users

    Returns:
        typing.List[UserType]: list of users
    """
    res = await user_svc.list_users(user_ids=user_ids or [])
    return [UserType.from_pydantic(u) for u in res]


async def create_user(user: UserCreateInput) -> UserType:
    """Create a new user

    Args:
        user (CreateUserType): User object

    Returns:
        UserType: User object
    """
    assert len(user.username) > 0, "username must not be empty"
    assert len(user.password) >= 8, "password must more or equal 8 characters"
    res = await user_svc.create_user(user.username, user.password, user.email)
    return UserType.from_pydantic(res)
