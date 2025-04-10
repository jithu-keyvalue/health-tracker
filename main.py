import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserOut, UserLogin, Token
from db.dependencies import get_db
from db.models import User
from utils.auth import hash_password, verify_password, create_access_token, get_current_user
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# Setup FastAPI app
app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/signup")
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

@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for email: {user.email}")

    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password_hash):
        logger.warning(f"Invalid credentials for email: {user.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": db_user.id})
    logger.info(f"Login successful for email: {user.email}")
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/profile", response_model=UserOut)
def get_profile(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    logger.info(f"Fetching profile for user: {current_user.email}")

    # Returning the current user
    return current_user