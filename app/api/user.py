from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from app.dependencies import get_current_user, get_db
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.services import user as user_service
from app.logging_config import logger

router = APIRouter()

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Signup attempt for email: {user.email}")
    return user_service.signup(db, user)

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for email: {user.email}")
    return user_service.login(db, user)

@router.get("/profile", response_model=UserOut)
def get_profile(current_user=Depends(get_current_user)):
    logger.info(f"Fetching profile for user: {current_user.email}")
    return current_user
