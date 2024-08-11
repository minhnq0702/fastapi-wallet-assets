"""Schema utilities"""
# -*- encoding; utf-8 -*-
import typing

import pydantic

T = typing.TypeVar("T")
def model_to_strawberry(model: pydantic.BaseModel, cls: typing.Type[T]) -> T:
    """Convert pydantic model to strawberry type"""
    _model = cls(**model.model_dump())
    return _model
