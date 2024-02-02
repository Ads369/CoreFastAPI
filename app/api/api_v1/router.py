from fastapi import APIRouter
from app.api.api_v1.endpoints.status import router as status_router


router = APIRouter()

router.include_router(status_router, prefix="/v1", tags=["Status"])
