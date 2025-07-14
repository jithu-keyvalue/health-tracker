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

- 🔧 Debugging SSE Issues  
    Check browser Network tab for SSE connection status.
    ```javascript
    // Log all received messages
    eventSource.onmessage = (event) => {
      console.log("SSE message:", JSON.parse(event.data));
    };
    
    // Check connection state
    console.log("ReadyState:", eventSource.readyState);
    // 0=CONNECTING, 1=OPEN, 2=CLOSED
    ```
    @Browser DevTools Network Tab

- 🔧 Redis Notification Debugging  
    Verify notifications are being published correctly.
    ```python
    # Check what's in Redis
    redis.lrange("notifications:user123", 0, -1)
    
    # Monitor Redis activity
    redis.monitor()  # Shows all Redis commands
    ```
    @Redis Debugging Commands

- 🚫 Common Notification Bugs  
    ```python
    # ✅ Correct user ID
    publish_notification(user_id, "Success!", "success")
    
    # ❌ Wrong identifier 
    publish_notification(file.id, "Success!", "success")
    ```

- 🚫 Async Context Issues  
    ```python
    # ✅ Proper exception handling
    try:
        result = await process_data()
        publish_notification(user_id, "Success!", "success")
    except Exception as e:
        publish_notification(user_id, "Failed!", "error")
    
    # ❌ Missing user context in catch block
    except Exception:
        publish_notification(wrong_id, "Failed!", "error")
    ```