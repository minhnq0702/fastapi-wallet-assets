"""GraphQL schema"""
# -*- encoding: utf-8 -*-
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from app.graphql.mutation import Mutation
from app.graphql.query import Query
from app.graphql.type_scalars import BigInt

_schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(
        auto_camel_case=True,
        # validate_queries=True,
    ),
    scalar_overrides={int: BigInt}
)
GraphQLRoute = GraphQLRouter(_schema)
