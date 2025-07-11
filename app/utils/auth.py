import os
import uuid
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from app.core.settings import settings
from argon2 import PasswordHasher, Type
from argon2.exceptions import VerifyMismatchError

# Password hashing setup with Argon2id
# Using OWASP recommended parameters:
# - Memory: 19 MiB (19,456 KiB)
# - Iterations: 2
# - Parallelism: 1
ph = PasswordHasher(
    time_cost=2,          # Number of iterations
    memory_cost=19456,    # 19 MiB in KiB
    parallelism=1,        # Number of parallel threads
    hash_len=32,          # Length of the hash in bytes
    type=Type.ID         # Use Argon2id variant
)

# JWT secret and algorithm setup
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = "HS256"

def hash_password(password: str):
    """Hash a password using Argon2id."""
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against a hash using Argon2id."""
    try:
        ph.verify(hashed_password, plain_password)
        return True
    except VerifyMismatchError:
        return False

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
    
