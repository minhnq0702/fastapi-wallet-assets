"""Init database connection"""
# -*- coding: utf-8 -*-
import typing
from functools import wraps
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel import MetaData, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

# TODO: load config from .env
DATABASE_URI = "postgresql+asyncpg://minhnguyen:@localhost/wallet-assets"
# db = Database(DATABASE_URL)
engine = create_async_engine(DATABASE_URI, echo=True)

DBMetadata = MetaData()
DBSession = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


async def init_models():
    """
    Init Database models meta
    """
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        # * Run create all SQLModel into database
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_tx() -> AsyncGenerator[AsyncSession, Any]:
    """Get DB session

    Yields:
        AsyncSession: Database session
    """
    async with DBSession() as _session:
        # async with _session.begin():
        yield _session

R = typing.TypeVar('R')
P = typing.ParamSpec('P')


def with_session(
        func: typing.Callable[..., typing.Coroutine[Any, Any, R]]
    ) -> typing.Callable[..., typing.Coroutine[Any, Any, R]]:
    """Wrapper get db session into kwargs

    Args:
        func (typing.Callable[..., typing.Coroutine[Any, Any, Any]]): _description_

    Returns:
        typing.Callable[..., typing.Coroutine[Any, Any, Any]]: _description_
    """
    @wraps(func)
    async def func_wrap(*args: P.args, **kwargs: P.kwargs):
        """
        Wrap function with db session
        """
        async with DBSession() as _session:
            res = await func(*args, session=_session, **kwargs)
            return res
    return func_wrap
