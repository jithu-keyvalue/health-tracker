from fastapi import Depends, APIRouter, HTTPException
from app.dependencies import get_current_user
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.db.models import User
from app.dependencies import get_db, get_current_user
from app.utils.auth import hash_password, verify_password, create_access_token
from app.logging_config import logger
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Signup attempt for email: {user.email}")
    
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        logger.warning(f"Email {user.email} already registered")
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = hash_password(user.password)
    
    new_user = User(name=user.name, email=user.email, password_hash=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    logger.info(f"User created: {new_user.email}")
    return {"message": "User created", "user": {"name": new_user.name, "email": new_user.email}}

@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for email: {user.email}")

    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        logger.warning(f"Invalid credentials for email: {user.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.id})
    logger.info(f"Login successful for email: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/profile", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user)):
    logger.info(f"Fetching profile for user: {current_user.email}")
    return current_user
