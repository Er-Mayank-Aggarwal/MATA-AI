from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger(__name__)


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception on {request.url}: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": "Internal server error", "detail": str(exc)},
    )


async def validation_exception_handler(request: Request, exc):
    return JSONResponse(
        status_code=422,
        content={
            "status": "error",
            "message": "Validation failed",
            "detail": exc.errors(),
        },
    )
