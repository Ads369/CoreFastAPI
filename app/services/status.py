from app.adapters.status_db import StatusDBAdapter
from app.adapters.status_redis import StatusRedisAdapter
from app.api.api_v1.schemas.status import GetStatusParam, GetStatusResponse
from app.services.base import MultiAdapterService


class GetStatus(MultiAdapterService):
    async def process(self, params: GetStatusParam) -> GetStatusResponse:
        result = GetStatusResponse(
            is_db_connection_ok=False,
            is_redis_connection_ok=False,
            db_msg=None,
            redis_msg=None,
        )

        # Объявления для TypeHints
        _db_adapter: StatusDBAdapter = self._adapters["db"]
        _redis_adapter: StatusRedisAdapter = self._adapters["redis"]

        # model_validate здесь!

        if params.check_db:
            try:
                _ = await _db_adapter.get_status(params)
                result.is_db_connection_ok = True
            except Exception as e:
                result.db_msg = str(e)

        if params.check_redis:
            try:
                _ = await _redis_adapter.get_keys("*")
                result.is_redis_connection_ok = True
            except Exception as e:
                result.redis_msg = str(e)

        return result
