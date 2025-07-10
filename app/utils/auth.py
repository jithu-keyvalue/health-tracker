import os
import uuid
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from app.core.settings import settings

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT secret and algorithm setup
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    expire = datetime.now(timezone.utc) + expires_delta
    
    if isinstance(data.get("sub"), uuid.UUID):
        data["sub"] = str(data["sub"])
    
    data["exp"] = expire
    
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> str:
    """Decode JWT token and return the user ID from the 'sub' field."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: missing user ID")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
