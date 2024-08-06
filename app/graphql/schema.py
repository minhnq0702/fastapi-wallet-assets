"""Define graphql schema."""
# -*- coding: utf-8 -*-
import typing

import strawberry
from strawberry.fastapi import GraphQLRouter

from app.graphql.user import User
from app.svc.user_svc import get_users


@strawberry.type
class Query:
    """GraphQL query object."""
    users: typing.List[User] = strawberry.field(resolver=get_users)


schema = strawberry.Schema(Query)
GraphQL_App = GraphQLRouter(schema)
