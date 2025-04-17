from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.utils.auth import verify_password, create_access_token
from app.schemas.user import UserCreate, UserLogin
from app.repositories import user as user_repository

def signup(db: Session, user_data: UserCreate):
    if user_repository.get_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_repository.create_user(db, user_data)

def login(db: Session, user_data: UserLogin):
    user = user_repository.get_by_email(db, user_data.email)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}
