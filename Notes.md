📝 Notes
--------

- 🌐 CORS (Cross-Origin Resource Sharing)
    Browser security feature that controls which websites can talk to your API.
    By default, browsers block requests between different origins for security.

    What is an origin?
    - Protocol + Domain + Port together
    - Example origins:
      - http://localhost:8000
      - http://localhost:8001
      - https://api.example.com

    Real-world example:
    1. You visit shadysite.com
    2. It tries to call api.yourbank.com
    3. Browser checks if api.yourbank.com allows
       requests from shadysite.com
    4. If not allowed → request blocked
    5. If allowed → request proceeds

    Enable in FastAPI:
    ```python
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"]
    )
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/cors/)

- 🌍 Static Server
    Serve frontend files locally
    ```bash
    cd frontend
    python3 -m http.server 3000
    ```
    [Docs](https://docs.python.org/3/library/http.server.html)

- 🔌 Fetch API
    Make HTTP requests from browser
    ```javascript
    const res = await fetch("/items", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });
    ```
    [Docs](https://developer.mozilla.org/docs/Web/API/Fetch_API)

- 📝 Logging Levels
    Choose right level for each event
    ```python
    logger.debug("Processing item")  # Details
    logger.info("Item saved")        # Normal
    logger.warning("Retry needed")   # Unusual
    logger.error("Save failed")      # Problem
    ```
    [Docs](https://docs.python.org/3/howto/logging.html)