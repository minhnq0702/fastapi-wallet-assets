# -*- encoding: utf-8 -*-
import datetime
import logging
from typing import Annotated

import strawberry

from app.graphql import type_login
from app.graphql.type_login import LoginResult
from app.graphql.type_scalars import JSON
from app.graphql.type_user import UserType, create_user
from app.graphql.type_wallet import WalletType, create_wallet

_logger = logging.getLogger(__name__)


@strawberry.type
class Mutation:
    """GraphQL mutation object."""
    @strawberry.mutation
    def ping(self, notify: str | None = 'test') -> JSON:
        """Ping GraphQL server

        Args:
            notify (str): notification message

        Returns:
        """
        _logger.info(".....ping %s", notify)
        # check_time = datetime.datetime.now().astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
        # check_time = datetime.datetime.now().astimezone(pytz.UTC)
        check_time = datetime.datetime.now()
        return JSON({
            "status": "successfully",
            "time": check_time.isoformat()
        })

    login: Annotated[LoginResult, "Login Result"] = strawberry.mutation(
        resolver=type_login.login
    )
    create_users: Annotated[UserType, "Created User"] = strawberry.mutation(
        resolver=create_user
    )

    create_wallet: Annotated[WalletType, "Created Wallet"] = strawberry.mutation(
        resolver=create_wallet
    )
    