import asyncio
from contextlib import ExitStack

import pytest
import redis.asyncio as redis
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.depends.redis_client import get_redis_client
from app.depends.sql_client import session_manager
from app.main import app as actual_app

BASE_URL = "http://127.0.0.1:8000"


@pytest.fixture(autouse=True)
def app():
    with ExitStack():
        yield actual_app


@pytest.fixture
def client(app) -> AsyncClient:
    return AsyncClient(app=app, base_url=BASE_URL)


@pytest.fixture
def test_client(app):
    with TestClient(app) as c:
        yield c


# Each test function rollback result
@pytest.fixture(scope="function", autouse=True)
async def transactional_session() -> AsyncSession:
    async with session_manager.session() as session:
        try:
            await session.begin()
            yield session
        finally:
            await session.rollback()


@pytest.fixture(scope="function")
async def db_session(transactional_session) -> AsyncSession:
    yield transactional_session


@pytest.fixture(scope="function")
async def redis_session():
    yield get_redis_client


@pytest.fixture
async def redis_client() -> redis.Redis:
    async for client in get_redis_client():
        return client
    
# Example fixture for Adapter
# @pytest.fixture(scope="function")
# async def device_adapter(db_session):
#     return DeviceAdapter(db_session=db_session)

# @pytest.fixture(scope="function")
# async def state_adapter(redis_client: redis.Redis):
#     return StateAdapter(redis_client=redis_client)