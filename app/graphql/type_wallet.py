import typing

import strawberry

from app.models.wallets import Wallets
from app.svc import wallet_svc


@strawberry.experimental.pydantic.type(model=Wallets)
class WalletType:
    """Wallet type."""
    id: typing.Optional[int]
    name: str
    owner_id: int
    active: bool
    balance: float


@strawberry.experimental.pydantic.input(model=Wallets)
class WalletCreateType:
    """Create wallet type."""
    name: str
    balance: typing.Optional[float] = 0.0


async def list_wallets() -> typing.List[WalletType]:
    """GraphQL list user's wallets

    Returns:
        typing.List[WalletType]: _description_
    """
    res = await wallet_svc.list_wallets()
    return [WalletType.from_pydantic(w) for w in res]


async def create_wallet(payload: WalletCreateType) -> typing.Annotated[WalletType, "Created wallet"]:
    """GraphQL create new wallet

    Returns:
        WalletType: new created wallet
    """
    # print(WalletCreateType(name='adfad'))
    wallet = Wallets(**payload.to_pydantic(
        owner_id=1, # ! only for dev testing. get from token/session userId
    ).model_dump())
    res = await wallet_svc.create_wallet(wallet)
    return WalletType.from_pydantic(res)
