import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse
from redis import Redis
from app.core.logging_config import logger
from app.core.settings import settings

redis = Redis.from_url(settings.REDIS_URL)

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Rate limit: 100 requests per 60 seconds
        key = f"ratelimit:{request.client.host}"
        requests = redis.incr(key)
        if requests == 1:
            redis.expire(key, 60)  # Expire in 60 seconds
        
        if requests > 100:
            logger.warning(f"Rate limit exceeded for {request.client.host}")
            return JSONResponse(
                status_code=429,
                content={"error": "Too many requests"}
            )

        return await call_next(request)
