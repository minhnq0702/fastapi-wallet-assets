"""Model users Definition"""
import typing

from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    """Users model"""
    id: typing.Optional[int] = Field(default=None, primary_key=True)
    username: str
    password: str
    email: str
