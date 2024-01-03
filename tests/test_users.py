import pytest as pytest
from src.config import settings

pytestmark = pytest.mark.anyio

async def test_get_single_user(db_session, async_client, product):
    pass

