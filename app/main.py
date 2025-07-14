from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api import health, user, observation, upload, notifications
from app.core.logging_config import logger
from app.core.exception_handlers import global_exception_handler, http_exception_handler
from app.core.rate_limit_middleware import RateLimitMiddleware

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.add_middleware(RateLimitMiddleware)

app.include_router(health.router)
app.include_router(user.router, prefix="/v1/users", tags=["users"])
app.include_router(observation.router, prefix="/v1/observations", tags=["observations"])
app.include_router(upload.router, prefix="/v1/files", tags=["files"])
app.include_router(notifications.router, prefix="/v1/notifications", tags=["notifications"])

logger.info("App initialized with routes")
