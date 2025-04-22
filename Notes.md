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
    - Clean, consistent error responses
    - Adds extra info to logs (request/user/url) (easy debugging)
    - Central place for alerting/instrumentation (send alert to developer)

🧱 Service + Repository Layers  
  - Clean separation of concerns:  
    - services/: business logic only (no HTTP, no DB code).  
    -  repositories/: raw DB access — only handles queries.  

  - Modularity  
    - You can change how you store data (Postgres → Mongo)
    - or how your business logic works without touching your route handlers.
  
  - Testability
    - You can test services/ with fake DB or mocks — no need to spin up FastAPI.
    - repositories/ can be tested in isolation for query correctness.