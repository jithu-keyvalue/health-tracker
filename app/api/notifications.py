from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.dependencies import get_current_user
from app.db.models import User
from app.services import notification as notification_service
from app.core.logging_config import logger

router = APIRouter()

@router.get("/stream")
async def stream_notifications(current_user: User = Depends(get_current_user)):
    """Stream Server-Sent Events for file processing notifications"""
    logger.info(f"Starting SSE stream for user {current_user.id}")
    
    return StreamingResponse(
        notification_service.stream_user_notifications(str(current_user.id)),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        }
    ) 