"""Init database connection"""
# -*- coding: utf-8 -*-
import typing
from contextlib import contextmanager
from functools import wraps
from typing import Any, Generator

# from sqlalchemy.engine import create_engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlmodel import MetaData, Session, SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession

# TODO: load config from .env
DATABASE_URI = "postgresql+asyncpg://minhnguyen:@localhost/wallet-assets"
sync_engine = create_engine("postgresql://minhnguyen:@localhost/wallet-assets")
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


@contextmanager
def get_tx() -> Generator[Session, Any, None]:
    """Get DB session

    Yields:
        AsyncSession: Database session
    """
    _session = Session(sync_engine, autocommit=False, autoflush=False)
    try:
        yield _session
    except Exception:
        _session.rollback()
        raise
    finally:
        _session.close()


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
