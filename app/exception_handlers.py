from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
from app.logging_config import logger

# HTTPException handler
async def http_exception_handler(request: Request, exc: HTTPException):
    logger.exception("HTTP exception occurred")
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "message": exc.detail
        },
    )

# Unhandled Exception handler
async def global_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled exception occurred")
    # send alert to monitoring team
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "Internal Server Error",
            "message": "Something went wrong. Please try again later."
        },
    )