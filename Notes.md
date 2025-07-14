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
    @MDN EventSource API

- 🔑 FastAPI SSE Response  
    Stream data using StreamingResponse with event format.
    ```python
    from fastapi.responses import StreamingResponse
    
    return StreamingResponse(
        stream_generator(),
        media_type="text/event-stream"
    )
    ```
    @FastAPI Streaming Response

- 🔑 Redis as Message Queue  
    Store notifications temporarily for user pickup.
    ```python
    redis.rpush("notifications:user123", json.dumps(data))
    redis.expire("notifications:user123", 300)
    ```
    @Redis Commands

- 🔑 Celery Task Notifications  
    Publish results when background tasks complete.
    ```python
    try:
        # Process file
        result = process_data()
        publish_notification(user_id, "Success!", "success")
    except Exception:
        publish_notification(user_id, "Failed!", "error")
    ```

- 🔑 Toast Notifications  
    Non-intrusive UI feedback that auto-disappears.
    ```javascript
    function showToast(message, type) {
      const toast = document.createElement("div");
      toast.style.cssText = `/* styling */`;
      setTimeout(() => toast.remove(), 3000);
    }
    ```
    @UX Toast Patterns

- 🚫 Common SSE Pitfalls  
    ```python
    # ✅ Proper SSE format
    yield f"data: {json.dumps(data)}\n\n"
    
    # ❌ Missing newlines
    yield f"data: {json.dumps(data)}"
    ```

- 🚫 Connection Management  
    ```javascript
    // ✅ Handle reconnection
    eventSource.onerror = () => {
      setTimeout(connectSSE, 5000);
    };
    
    // ❌ No error handling
    eventSource.onmessage = handler;
    ```