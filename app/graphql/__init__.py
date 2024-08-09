"""Import all service modules."""

from typing import NewType

import strawberry

# TODO: move to scalars.py
JSON = strawberry.scalar(
    NewType("JSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)
