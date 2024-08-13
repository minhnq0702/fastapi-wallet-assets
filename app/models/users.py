"""Model users Definition"""
import datetime
import typing

import sqlalchemy as sa
from sqlmodel import Field, Relationship, SQLModel

if typing.TYPE_CHECKING:
    from app.models.wallets import Wallets

class Users(SQLModel, table=True):
    """Users model"""
    id: typing.Optional[int] = Field(
        default=None,
        primary_key=True
    )
    username: str = Field(max_length=64)
    password: str
    email: str
    created_date: datetime.datetime | None = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)),
        default_factory=datetime.datetime.now
    )
    updated_date: datetime.datetime | None = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)),
        default_factory=datetime.datetime.now
    )
    wallets: typing.List["Wallets"] = Relationship(
        back_populates="owner")
