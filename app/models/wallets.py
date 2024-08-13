# -*- encoding: utf-8 -*-
import datetime
import typing

import sqlalchemy as sa
from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

if typing.TYPE_CHECKING:
    from app.models.users import Users

class Wallets(SQLModel, table=True):
    """Wallets model"""
    __table_args__ = (UniqueConstraint("name", "owner_id"),)

    id: int = Field(
        default=None,
        primary_key=True)
    name: str = Field(
        default=None,
        nullable=False,
        max_length=64)
    balance: float = Field(
        default=0.0)
    owner_id: int = Field(
        foreign_key="users.id",
        nullable=False)
    owner: "Users" = Relationship(
        back_populates="wallets")
    active: bool = Field(
        default=True,
    )
    created_date: datetime.datetime | None = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)),
        default_factory=datetime.datetime.now)
    updated_date: datetime.datetime | None = Field(
        sa_column=sa.Column(sa.DateTime(timezone=True)),
        default_factory=datetime.datetime.now)
