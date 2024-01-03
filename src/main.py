from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

from src.api.api import api_router
from src.db import engine
from src.config import settings
from src.exceptions import CustomException
from src.logger import get_logger

logger = get_logger("app")

def create_app() -> FastAPI:

    path_prefix = "/dev" if settings.ENV == "dev" else ""
    application = FastAPI(
        title="Test DA",
        description="Тестовое задание",
        version=settings.VERSION,
        root_path=path_prefix,
        openapi_prefix=path_prefix,
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3002"],
        allow_credentials=True,
        allow_methods=["GET", "OPTIONS", "PUT", "POST", "DELETE", "PATCH"],
        allow_headers=["timezone", "authcode", "lang", "sessionId", "authorization", "uber-trace-id"],
    )

    application.include_router(api_router, prefix="/api")

    @application.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException) -> JSONResponse:
        return JSONResponse(
            content={"status": exc.status_code, "code": exc.code, "message": f"{exc.message}"},
            status_code=exc.status_code,
        )

    return application


app = create_app()
