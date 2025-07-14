📝 Notes
-----
- 🔑 Server-Sent Events (SSE)  
    One-way HTTP stream from server to client for real-time updates.
    ```javascript
    // Browser keeps connection open, receives data pushes
    const eventSource = new EventSource('/notifications');
    eventSource.onmessage = (event) => {
      const notification = JSON.parse(event.data);
      showToast(notification.message);
    };
    ```
    [EventSource API][1]

- 🔑 Complete SSE Setup  
    Frontend connects, backend streams, Redis queues messages.
    ```python
    # Backend: Create streaming endpoint
    @router.get("/notifications")
    async def stream_notifications(token: str = Query(...)):
        user_id = decode_token(token)
        return StreamingResponse(
            stream_user_notifications(user_id),
            media_type="text/event-stream",
            headers={"Cache-Control": "no-cache"}
        )
    
    # Stream generator polls Redis for messages
    async def stream_user_notifications(user_id: str):
        while True:
            msg = redis.lpop(f"notifications:{user_id}")
            if msg:
                yield f"data: {msg}\n\n"
            await asyncio.sleep(1)
    ```
    [FastAPI Streaming][2]

- 🔑 Publishing Messages  
    Background tasks push notifications to Redis queues.
    ```python
    def publish_notification(user_id: str, message: str, type: str):
        data = {"message": message, "type": type}
        redis.rpush(f"notifications:{user_id}", json.dumps(data))
        redis.expire(f"notifications:{user_id}", 300)
    
    # Usage in Celery task
    @celery_app.task
    def process_file(user_id: str):
        try:
            # Process file...
            publish_notification(user_id, "File processed!", "success")
        except Exception:
            publish_notification(user_id, "Processing failed", "error")
    ```
    [Redis Commands][3]

- 🔑 Client Connection Handling  
    Handle disconnects and auto-reconnect for reliability.
    ```javascript
    function connectSSE() {
        const eventSource = new EventSource('/notifications?token=xyz');
        
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            showToast(data.message, data.type);
        };
        
        eventSource.onerror = () => {
            eventSource.close();
            setTimeout(connectSSE, 5000);  // Reconnect after 5s
        };
    }
    ```
    [EventSource Events][4]

- 🔑 Required Dependencies  
    Install Redis and FastAPI for SSE implementation.
    ```bash
    pip install fastapi redis celery
    
    # Docker setup
    services:
      redis:
        image: redis
        ports: ["6379:6379"]
    ```
    [FastAPI Docs][5]

- 🚫 SSE Format Requirements  
    ```python
    # ✅ Proper SSE format - must end with \n\n
    yield f"data: {json.dumps(data)}\n\n"
    
    # ❌ Missing newlines breaks client parsing
    yield f"data: {json.dumps(data)}"
    
    # ✅ Correct media type
    media_type="text/event-stream"
    
    # ❌ Wrong media type breaks EventSource
    media_type="application/json"
    ```

[1]: https://developer.mozilla.org/en-US/docs/Web/API/EventSource
[2]: https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse
[3]: https://redis.io/commands/rpush/
[4]: https://developer.mozilla.org/en-US/docs/Web/API/EventSource/error_event
[5]: https://fastapi.tiangolo.com/