"""Init database connection"""
# -*- coding: utf-8 -*-
from typing import Any, AsyncGenerator

from databases import Database
from sqlalchemy import MetaData
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from sqlalchemy.orm import declarative_base

# TODO: load config from .env
DATABASE_URL = "postgresql+asyncpg://minhnguyen:@localhost/wallet-assets"
db = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)

DBMetadata = MetaData()
DBSession = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base(metadata=DBMetadata)
# class Base(AsyncAttrs, DeclarativeBase):
#     pass


async def get_tx() -> AsyncGenerator[AsyncSession, Any]:
    """Get DB session

    Yields:
        AsyncSession: Database session
    """
    async with DBSession() as _session:
        yield _session
