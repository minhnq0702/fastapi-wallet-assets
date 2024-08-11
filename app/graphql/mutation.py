# -*- encoding: utf-8 -*-
import datetime
import logging
import typing

import strawberry

from app.graphql.scalars import JSON
from app.graphql.type_user import UserType, create_user

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
        return JSON({
            "status": "successfully",
            "time": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%s")
        })

    # createUsers: typing.Annotated[typing.Union[UserType, None], "Created user"] = strawberry.mutation(
    #     resolver=create_user,
    # )
    create_users: typing.Annotated[typing.Union[UserType, None], "Created User"] = strawberry.mutation(
        resolver=create_user
    )
    
