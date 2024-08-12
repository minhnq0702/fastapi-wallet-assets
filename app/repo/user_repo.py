"""User repository module."""
# -*- encoding: utf-8 -*-
import typing

import pydantic
from sqlmodel import col, select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.users import Users
from app.repo import database


class UserFlow(pydantic.BaseModel):
    """Flow control how to query Users
    """
    by_id: typing.Optional[typing.List[int]] = None
    by_username: typing.Optional[str] = None


@database.with_session
async def list_users(ids: typing.Union[typing.List[int], None] = None, **kwargs) -> typing.Sequence[Users]:
    """List Users from DB
    Args:
        ids (list[int]): list of user id
    Returns:
        typing.List[Users]: list users
    """
    session: AsyncSession = kwargs["session"]
    # tx = await session.connection(execution_options={
    #     "isolation_level": "SERIALIZABLE"
    # })
    q = select(Users)
    if ids:
        q = q.where(col(Users.id).in_(ids))
    # res = await tx.execute(q)
    res = await session.exec(q, execution_options={
        "isolation_level": "SERIALIZABLE"
    })
    # await tx.commit()
    return res.all()


@database.with_session
async def create_user(username: str, password: str, email: str, **kwargs) -> Users:
    """Create a new user

    Args:
        username (str): Username
        password (str): Password
        email (str): Email

    Returns:
        Users: User object
    """
    session: AsyncSession = kwargs["session"]
    user = Users(username=username, password=password, email=email)
    session.add(user)
    # * must persit and call refresh to fetch new data (ID) from db
    await session.commit()
    await session.refresh(user)
    return user


@database.with_session
async def get_user(flow: UserFlow, **kwargs) -> typing.Optional[Users]:
    """Get user by condition

    Args:
        flow (UserFlow): User query condition
    Returns:
        Users: found user
    """
    session: AsyncSession = kwargs["session"]
    q = select(Users)
    if flow.by_username:
        q = q.where(Users.username == flow.by_username)
    res = await session.exec(q)
    user = res.first()
    return user
