📝 Notes
--------

- 🏗️ Clean Architecture
    Separate concerns
    ```python
    # Routes - handle HTTP
    @router.get("/items")
    def list_items(user = Depends(get_user)):
        return service.get_items(user.id)

    # Services - business logic
    def get_items(user_id: str):
        items = repo.get_by_user(user_id)
        return [process(item) for item in items]

    # Repos - data access
    def get_by_user(user_id: str):
        return db.query(Item).filter_by(user_id=user_id)
    ```
    Each layer has one job
    [Docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

- 🛡️ Exception Handler
    Global error handling
    ```python
    @app.exception_handler(Exception)
    async def handler(request: Request, exc: Exception):
        # Log rich context for debugging
        logger.error(
            "Unhandled exception occurred",
            extra={
                "url": request.url.path,
                "user": request.state.user.email,
                "method": request.method,
                "error": str(exc)
            }
        )

        # Send alert for critical errors
        if isinstance(exc, DatabaseError):
            alert_developer(request, exc)

        # Clean response to user
        return JSONResponse(
            status_code=500,
            content={
                "error": "Could not process request",
                "code": "INTERNAL_ERROR"
            }
        )
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/handling-errors/)