from typing import Any, TypeAlias

from sqlalchemy import (
    select,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.api_v1.schemas.status import GetStatusParam



class StatusDBAdapter:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_status(self, params: GetStatusParam) -> list:

        stmt = select(1)

        result = []

        query = await self.db_session.execute(stmt)
        rows = query.all()

        result = [row._asdict() for row in rows]
        return result
