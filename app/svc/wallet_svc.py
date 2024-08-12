# -*- encoding: utf-8 -*-

from typing import Sequence

from app.models.wallets import Wallets
from app.repo import wallet_repo


async def list_wallets() -> Sequence[Wallets]:
    """List user's wallets

    Returns:
        typing.Sequence[Wallets]: user's wallets
    """
    return await wallet_repo.list_wallets()


async def create_wallet(wallet: Wallets) -> Wallets:
    """Service create new wallet

    Args:
        wallet (Wallets): created wallet
    """
    res = await wallet_repo.create_wallet(wallet)
    return res
