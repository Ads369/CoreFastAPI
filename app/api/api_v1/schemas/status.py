from typing import Optional

from pydantic import (
    BaseModel,
    Field,
)


class GetStatusParam(BaseModel):
    """
    Параметры для запроса к API.
    """

    check_db: Optional[bool] = Field(default=None)
    check_redis: Optional[bool] = Field(default=None)


class GetStatusResponse(BaseModel):
    """
    Модель данных, которая будет отправлена в ответе от API.
    """

    is_db_connection_ok: bool
    is_redis_connection_ok: bool
    db_msg: Optional[str]
    redis_msg: Optional[str]
