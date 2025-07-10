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

- 🔄 Async Database
    Modern SQLAlchemy with asyncpg
    ```python
    # Create engine and session
    engine = create_async_engine(
        "postgresql+asyncpg://user:pass@host/db"
    )
    
    async def get_db():
        async with AsyncSessionLocal() as session:
            yield session
    
    # Use in routes
    @router.get("/items")
    async def list_items(db: AsyncSession):
        stmt = select(Item)
        result = await db.execute(stmt)
        return result.scalars().all()
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

    🎯 Exercise 1: Debug the N+1 Query
    ```python
    @router.get("/users/with-observations")
    async def get_users_with_obs(db: AsyncSession):
        # This has an N+1 query problem
        stmt = select(User)
        result = await db.execute(stmt)
        users = result.scalars().all()
        
        return [{
            "id": user.id,
            "name": user.name,
            "observations": await get_user_observations(db, user)
        } for user in users]
    ```
    Task: Fix the N+1 query issue by using proper SQLAlchemy relationship loading
    Hint: Look into selectinload() or joinedload()

    🎯 Exercise 2: Implement Pagination
    ```python
    @router.get("/observations/recent")
    async def get_recent_obs(
        db: AsyncSession,
        current_user: User
    ):
        stmt = select(Observation).where(
            Observation.user_id == current_user.id
        ).order_by(Observation.date.desc())
        result = await db.execute(stmt)
        return result.scalars().all()
    ```
    Task: Add offset pagination with page size of 10
    Requirements:
    - Add page parameter (default=1)
    - Return total count
    - Return has_more flag
    Hint: Look into func.count() and limit()/offset()