from typing import Annotated, Any

import redis.asyncio as redis
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.status_db import StatusDBAdapter
from app.adapters.status_redis import StatusRedisAdapter
from app.api.api_v1.schemas.status import GetStatusParam, GetStatusResponse
from app.depends.redis_client import get_redis_client
from app.depends.sql_client import get_db_session
from app.services.status import GetStatus

router = APIRouter()


@router.get(
    "/status",
    summary="Проверка статуса системы",
    response_model=GetStatusResponse,
)
async def check_status(
    params: Annotated[GetStatusParam, Depends(GetStatusParam)],
    redis_client: Annotated[redis.Redis, Depends(get_redis_client)],
    db_session: Annotated[AsyncSession, Depends(get_db_session)],
) -> Any:
    adapters = {
        "redis": StatusRedisAdapter(redis_client=redis_client),
        "db": StatusDBAdapter(db_session=db_session),
    }

    result = await GetStatus(adapters).process(params=params)
    return result
