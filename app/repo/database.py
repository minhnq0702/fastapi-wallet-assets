"""Init database connection"""
# -*- coding: utf-8 -*-
from typing import Any, AsyncGenerator, Generator

# from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

# TODO: load config from .env
DATABASE_URL = "postgresql+asyncpg://minhnguyen:@localhost/wallet-assets"
# db = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URL)

DBMetadata = MetaData()
DBSession = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)
# Base = declarative_base(metadata=DBMetadata)

async def inti_db():
    """
    INIT DB
    """
    # SQLModel.metadata.create_all(engine)



async def get_tx() -> AsyncGenerator[AsyncSession, Any]:
    """Get DB session

    Yields:
        AsyncSession: Database session
    """
    async with DBSession() as _session:
        yield _session
