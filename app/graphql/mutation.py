# -*- encoding: utf-8 -*-
import typing

import strawberry

from app.graphql.type_user import CreateUserType, UserType, create_user


@strawberry.type
class Mutation:
    """GraphQL mutation object."""
    @strawberry.mutation
    def ping(self, notify: str | None = 'test') -> None:
        """Ping GraphQL server

        Args:
            notify (str): notification message

        Returns:
        """
        print("ping", notify)

    # createUsers: typing.Annotated[typing.Union[UserType, None], "Created user"] = strawberry.mutation(
    #     resolver=create_user,
    # )
    create_users: typing.Annotated[typing.Union[UserType, None], "Created User"] = strawberry.mutation(
        resolver=create_user
    )
    
