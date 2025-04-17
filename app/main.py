from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.api import user, observation, upload
from app.logging_config import logger
from app.exception_handlers import global_exception_handler, http_exception_handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(observation.router, prefix="/observations", tags=["observations"])
app.include_router(upload.router, prefix="/files", tags=["files"])

logger.info("App initialized with routes")
