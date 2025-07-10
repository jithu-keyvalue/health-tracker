from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import AsyncSessionLocal
from fastapi import Request, Depends, HTTPException
from app.db.models import User
from app.utils.auth import decode_token

# Dependency for async DB session
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Update get_current_user to use async session
async def get_current_user(request: Request, db: AsyncSession = Depends(get_db)) -> User:
    token = request.headers.get("Authorization")
    if not token or not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    user_id = decode_token(token.split(" ")[1])
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Use select to get user
    from sqlalchemy import select
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user