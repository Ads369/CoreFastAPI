import pytest
from sqlalchemy import select

from app.core.settings import settings


@pytest.mark.asyncio
async def test_db_connect(db_session):
    session = db_session
    result = await session.execute(select(1))
    result = result.all()
    assert result == [(1,)], "Database is not available"


# @pytest.mark.asyncio
# async def test_redis_connect(redis_client):
#     assert redis_client is not None
#     assert await redis_client.ping() is True, "Redis is not available"
#     assert len(await redis_client.keys()) > 0, "Redis is empty"
#     assert (
#         len(await redis_client.keys("*")) > 0
#     ), "Necessary keys are not found in Redis"
