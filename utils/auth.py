from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import Request, Depends, HTTPException
from sqlalchemy.orm import Session
from db.dependencies import get_db
from db.models import User
import os
import uuid

# Password hashing setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT secret and algorithm setup
SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")
ALGORITHM = "HS256"

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create access token

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)):
    # Generate expiration time
    expire = datetime.now(timezone.utc) + expires_delta
    
    # Ensure 'sub' is a string if it's UUID
    if isinstance(data.get("sub"), uuid.UUID):
        data["sub"] = str(data["sub"])
    
    # Add expiration time to data
    data["exp"] = expire
    
    # Encode and return JWT
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    # Extract Authorization header
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth.split(" ")[1]  # Get token from "Bearer <token>"
    
    try:
        # Decode the token and get the user_id from the payload
        payload = decode_token(token)
        user_id = payload.get("sub")  # "sub" typically contains user identifier
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    # Fetch the user from the DB
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user