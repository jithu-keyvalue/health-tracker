📝 Notes
-----
- 🔑 Server-Sent Events (SSE)  
    HTTP connection that streams data from server to client.
    ```javascript
    const eventSource = new EventSource('/stream');
    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
    };
    ```
    https://developer.mozilla.org/en-US/docs/Web/API/EventSource

- 🔑 FastAPI SSE Response  
    Stream data using StreamingResponse with event format.
    ```python
    from fastapi.responses import StreamingResponse
    
    return StreamingResponse(
        stream_generator(),
        media_type="text/event-stream"
    )
    ```
    https://fastapi.tiangolo.com/advanced/custom-response/#streamingresponse

- 🔑 Redis as Message Queue  
    Store notifications temporarily for user pickup.
    ```python
    redis.rpush("notifications:user123", json.dumps(data))
    redis.expire("notifications:user123", 300)
    ```
    https://redis.io/commands/rpush/

- 🔑 Celery Task Notifications  
    Publish results when background tasks complete.
    ```python
    try:
        result = process_data()
        publish_notification(user_id, "Success!", "success")
    except Exception:
        publish_notification(user_id, "Failed!", "error")
    ```

- 🚫 Common SSE Pitfalls  
    ```python
    # ✅ Proper SSE format
    yield f"data: {json.dumps(data)}\n\n"
    
    # ❌ Missing newlines
    yield f"data: {json.dumps(data)}"
    ```