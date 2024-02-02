from collections.abc import AsyncIterator

import redis.asyncio as redis

from app.core.settings import settings


redis_pool = redis.ConnectionPool.from_url(
    url=str(settings.REDIS_URL), max_connections=10, decode_responses=True
)


async def get_redis_client() -> redis.Redis:
    async with redis.Redis(connection_pool=redis_pool) as redis_client:
        yield redis_client
