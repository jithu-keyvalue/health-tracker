📝 Notes
--------

- ⚙️ Settings
    Centralize config with Pydantic
    ```python
    class Settings(BaseSettings):
        DB_HOST: str
        REDIS_URL: str
        
        class Config:
            env_file = ".env"
    
    settings = Settings()  # Validates on load
    ```
    [Docs](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

- 🔄 Middleware
    Run code before/after requests
    ```python
    class CustomMiddleware(BaseHTTPMiddleware):
        async def dispatch(self, request, call_next):
            # Do something before request
            response = await call_next(request)
            # Do something after request
            return response
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/middleware/)

- 🌐 API Version
    Future-proof routes
    ```python
    # Routes under /v1
    app.include_router(
        users,
        prefix="/v1/users"
    )
    
    # Can add /v2 later
    if settings.enable_v2:
        app.include_router(
            users_v2,
            prefix="/v2/users"
        )
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/)