"""Scalar types"""

from datetime import datetime
from typing import NewType

import pytz
import strawberry

JSON = strawberry.scalar(
    NewType("JSON", object),
    description="The `JSON` scalar type represents JSON values as specified by ECMA-404",
    serialize=lambda v: v,
    parse_value=lambda v: v,
)


EpochDateTime = strawberry.scalar(
    NewType("EpochDateTime", datetime),
    serialize=lambda value: int(value.timestamp()),
    parse_value=lambda value: datetime.fromtimestamp(int(value), pytz.utc),
)
