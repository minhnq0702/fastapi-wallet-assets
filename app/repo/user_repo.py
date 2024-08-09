"""User repository module."""
# -*- encoding: utf-8 -*-
import typing

from sqlmodel import col, select

from app.models.users import Users
from app.repo import database


async def get_users(ids: typing.Union[typing.List[int], None] = None) -> typing.List[Users]:
    """List Users from DB

    Returns:
        typing.List[Users]: _description_
    """
    dbc = database.get_tx()
    db = await anext(dbc)
    # tx = await db.connection(execution_options={
    #     "isolation_level": "SERIALIZABLE"
    # })
    query = select(Users)
    if ids:
        query = query.where(col(Users.id).in_(ids))
    res = await db.exec(query, execution_options={
        "isolation_level": "SERIALIZABLE"
    })
    # await tx.commit()
    await db.close()
    return list(res)


async def create_user(username: str, password: str, email: str) -> Users:
    """Create a new user

    Args:
        username (str): Username
        password (str): Password

    Returns:
        Users: User object
    """
    dbc = database.get_tx()
    db = await anext(dbc)
    user = Users(username=username, password=password, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
