# -*- coding: utf-8 -*-
import typing

import strawberry

from app.graphql.type_user import UserType, list_users
from app.graphql.type_wallet import WalletType, list_wallets


@strawberry.type
class Query:
    """GraphQL query object."""
    listUsers: typing.List[UserType] = strawberry.field(
        resolver=list_users,
    )

    listWallets: typing.List[WalletType] = strawberry.field(
        resolver=list_wallets
    )
