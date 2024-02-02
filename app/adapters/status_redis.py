import redis.asyncio as redis


class StatusRedisAdapter:
    def __init__(self, redis_client: redis.Redis):
        self.redis_client = redis_client

    async def get_keys(self, key_suffix: str | int) -> str | None:
        return await self.redis_client.get(
            name=self._get_redis_messages_key(key_suffix=key_suffix),
        )

    @staticmethod
    def _get_redis_messages_key(key_suffix: str | int) -> str:
        return f"{key_suffix}".lower()
