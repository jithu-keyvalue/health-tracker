from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserLogin, UserOut, Token
from app.repositories import user as user_repo
from app.utils.auth import hash_password, verify_password, create_access_token

async def signup(db: AsyncSession, user_data: UserCreate) -> dict:
    if await user_repo.get_by_email(db, user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash password before storing
    user_data.password = hash_password(user_data.password)
    user = await user_repo.create(db, user_data)
    
    return {
        "message": "User created",
        "user": UserOut.model_validate(user)
    }

async def login(db: AsyncSession, user_data: UserLogin) -> Token:
    user = await user_repo.get_by_email(db, user_data.email)
    if not user or not verify_password(user_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": str(user.id)})
    return Token(access_token=token, token_type="bearer")
