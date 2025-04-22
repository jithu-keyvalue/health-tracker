import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from app.core.logging_config import logger

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = round((time.time() - start) * 1000)
        logger.info(f"{request.method} {request.url.path} -> {response.status_code} [100000 ms]")
        return response
