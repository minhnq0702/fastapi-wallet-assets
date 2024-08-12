import typing

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.models.wallets import Wallets
from app.repo import database


@database.with_session
async def list_wallets(**kwargs) -> typing.Sequence[Wallets]:
    """List wallets

    Returns:
        typing.Sequence[Wallets]: List of user wallets
    """
    session: AsyncSession = kwargs["session"]
    if not session:
        return []

    q = select(Wallets)
    res = await session.exec(q)
    return res.all()


@database.with_session
async def create_wallet(wallet: Wallets, **kwargs) -> Wallets:
    """
    Create new wallet
    Args:
        wallet (Wallets): wallet obj to create
    """
    session: AsyncSession = kwargs["session"]
    session.add(wallet)
    await session.commit()
    await session.refresh(wallet)
    return wallet
