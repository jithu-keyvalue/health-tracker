import json
import asyncio
from typing import AsyncGenerator
from redis import Redis
from app.core.settings import settings
from app.core.logging_config import logger

redis = Redis.from_url(settings.REDIS_URL)

async def stream_user_notifications(user_id: str) -> AsyncGenerator[str, None]:
    """Stream notifications for a specific user via SSE"""
    logger.info(f"Starting notification stream for user {user_id}")
    
    while True:
        try:
            # Check for new notifications
            notification_key = f"notifications:{user_id}"
            notification_data = redis.lpop(notification_key)
            
            if notification_data:
                notification = json.loads(notification_data)
                logger.info(f"Sending notification to user {user_id}: {notification}")
                
                # Format as SSE event
                yield f"data: {json.dumps(notification)}\n\n"
            
            # Wait before checking again
            await asyncio.sleep(1)
            
        except Exception as e:
            logger.error(f"Error in notification stream: {e}")
            await asyncio.sleep(5)

def publish_notification(user_id: str, message: str, type: str = "info"):
    """Publish notification to Redis for specific user"""
    import time
    
    notification = {
        "message": message,
        "type": type,
        "timestamp": time.time()
    }
    
    notification_key = f"notifications:{user_id}"
    redis.rpush(notification_key, json.dumps(notification))
    redis.expire(notification_key, 300)  # Expire in 5 minutes
    
    logger.info(f"Published notification for user {user_id}: {message}") 