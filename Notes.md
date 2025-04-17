📝 Notes
--------

- 📝 Global Exception Handler  
  Catch all unhandled exceptions and respond cleanly.

  ```python
  @app.exception_handler(Exception)
  async def global_exception_handler(request: Request, exc: Exception):
    logger.exception(f"Unhandled error on {request.url.path}: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})
  ```

  📦 Benefits:
    - Does not expose implementation details, internal error messages. (professional, safe)
    - Clean, consistent error responses (no raw tracebacks in client)
    - Adds extra info to logs (request/user/url) (easy debugging)
    - Central place for alerting/instrumentation(send alert to developer)
