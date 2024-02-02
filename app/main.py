from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from app.api.router import router as api_router
from app.core.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
    unhandled_exception_handler,
)
from app.core.middleware import log_request_middleware
from app.core.settings import settings

app = FastAPI(
    debug=settings.DEBUG,
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    root_path=settings.ROOT_PATH,
)

# MiddleWare for pretty logs for FastApi
app.middleware("http")(log_request_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

app.include_router(api_router, prefix=settings.API_PREFIX)
