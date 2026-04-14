# -*- encoding: utf-8 -*-
import pytest
import pytest_asyncio
from sqlmodel import SQLModel

from app.repo import user_repo


@pytest.mark.asyncio
async def test_list_users():
    """Test list users
    """
    res = await user_repo.list_users()
    print("==>", res)
    assert res