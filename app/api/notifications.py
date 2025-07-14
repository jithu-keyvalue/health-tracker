from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_db
from app.db.models import User
from app.services import notification as notification_service
from app.core.logging_config import logger
from app.utils.auth import decode_token
from sqlalchemy import select

router = APIRouter()

@router.get("/stream")
async def stream_notifications(
    token: str = Query(..., description="Bearer token for authentication"),
    db: AsyncSession = Depends(get_db)
):
    """Stream Server-Sent Events for file processing notifications"""
    # Decode token to get user
    user_id = decode_token(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    # Verify user exists
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    logger.info(f"Starting SSE stream for user {user.id}")
    
    return StreamingResponse(
        notification_service.stream_user_notifications(str(user.id)),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    ) 