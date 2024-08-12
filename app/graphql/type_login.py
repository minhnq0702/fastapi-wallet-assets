# -*- encoding: utf-8 -*-
from typing import Annotated, Union

import strawberry

from app.graphql.type_user import UserType
from app.svc import user_svc


@strawberry.type
class LoginSuccessType:
    """Login successfully type."""
    user: UserType
    token: str


@strawberry.type
class LoginFailType:
    """Login failed type."""
    msg: str


@strawberry.input
class LoginInput:
    """Login input."""
    username: str
    password: str


LoginResult = Union[LoginSuccessType, LoginFailType, None]
async def login(payload: LoginInput) -> Annotated[LoginResult, strawberry.union("LoginResult")]:
    """Login

    Returns:
        LoginResult (LoginResult): Login
    """
    res = await user_svc.login(payload.username, payload.password)
    if not res:
        return LoginFailType(msg='Login fail')
    return LoginSuccessType(
        user=UserType.from_pydantic(res),
        token='this-is-token'
    )
