import pytest

from app.api.api_v1.schemas.status import GetStatusParam, GetStatusResponse

@pytest.mark.asyncio
async def test_healthcheck(client):
    response = await client.get("/docs")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_get_status(client):
    params = GetStatusParam(check_db=True, check_redis=False)
    response = await client.get("/api/v1/status", params=params.model_dump())
    assert response.status_code == 200

    result = GetStatusResponse(**response.json())
    assert result.is_db_connection_ok is True
