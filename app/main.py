from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import user, observation
from app.logging_config import logger

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(observation.router, prefix="/observations", tags=["observations"])

logger.info("App initialized with routes")
