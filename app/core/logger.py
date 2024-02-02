import logging

from app.core.settings import settings
from sqlalchemy.dialects import postgresql

# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

logger = logging.getLogger("uvicorn")
level = logging.getLevelName(settings.LOG_LEVEL)
logger.setLevel(logging.getLevelName(level))


def logging_sql(stmt):
    logger.debug(str(stmt.compile(
        dialect=postgresql.dialect(),
        compile_kwargs={"literal_binds": True})))