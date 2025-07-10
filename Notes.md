📝 Notes
--------

- 🔄 Async Database
    Basic setup
    ```python
    # Engine and session
    engine = create_async_engine(
        "postgresql+asyncpg://user:pass@host/db"
    )
    async_session = async_sessionmaker(engine)
    ```

    Query patterns
    ```python
    # Basic select
    stmt = select(User).where(User.id == 1)
    user = await db.scalar(stmt)

    # Multiple results
    stmt = select(Item).order_by(Item.id)
    items = await db.scalars(stmt)
    ```

    Session usage
    ```python
    # ✅ Context manager
    async with async_session() as db:
        await db.scalar(stmt)

    # ❌ Manual cleanup
    db = async_session()
    await db.close()
    ```

    FastAPI integration
    ```python
    async def get_db():
        async with async_session() as db:
            yield db

    @router.get("/items")
    async def list_items(db: AsyncSession):
        return await db.scalars(select(Item))
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)