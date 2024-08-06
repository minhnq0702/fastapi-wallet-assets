"""User GraphQL schema."""
# -*- coding: utf-8 -*-
import strawberry
from pydantic import BaseModel


@strawberry.type
class User(BaseModel):
    """User object."""
    username: str
    password: str
    email: str
