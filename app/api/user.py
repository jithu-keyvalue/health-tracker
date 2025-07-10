from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_current_user, get_db
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.services import user as user_service
from app.core.logging_config import logger

router = APIRouter()

@router.post("/signup", response_model=dict)
async def signup(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
) -> dict:
    logger.info("Processing signup request")
    return await user_service.signup(db, user)

@router.post("/login", response_model=Token)
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(get_db)
) -> Token:
    logger.info("Processing login request")
    return await user_service.login(db, user)

@router.get("/profile", response_model=UserOut)
async def get_profile(
    current_user = Depends(get_current_user)
) -> UserOut:
    await logger.info(f"Fetching profile for user {current_user.id}")
    return UserOut.model_validate(current_user)
