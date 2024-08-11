# -*- encoding: utf-8 -*-
import datetime
import logging
import typing

import pytz
import strawberry

from app.graphql.type_scalars import JSON
from app.graphql.type_user import UserType, create_user
from app.tools import DEFAULT_DATETIME_FORMAT

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
            "time": check_time.strftime(DEFAULT_DATETIME_FORMAT)
        })

    # createUsers: typing.Annotated[typing.Union[UserType, None], "Created user"] = strawberry.mutation(
    #     resolver=create_user,
    # )
    create_users: typing.Annotated[typing.Union[UserType, None], "Created User"] = strawberry.mutation(
        resolver=create_user
    )
    
