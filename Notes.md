📝 Notes
--------

- 🔄 Async SQLAlchemy
    Basic query with async/await
    ```python
    # Simple select
    result = await db.scalars(
        select(User).where(User.id == 1)
    )
    ```

    Session management
    ```python
    # ✅ Context manager
    async with AsyncSession() as db:
        await db.scalars(stmt)
    
    # ❌ Manual cleanup
    db = AsyncSession()
    await db.close()
    ```

    Loading relationships
    ```python
    # Basic: Separate queries
    user = await db.scalar(select(User))
    items = await db.scalars(
        select(Item).where(Item.user_id == user.id)
    )

    # Better: Join load
    user = await db.scalar(
        select(User).options(
            joinedload(User.items)
        )
    )
    items = user.items  # Already loaded
    ```

    Pagination pattern
    ```python
    # Count total
    count = await db.scalar(
        select(func.count()).select_from(Item)
    )
    
    # Get page
    items = await db.scalars(
        select(Item)
        .limit(10)
        .offset((page - 1) * 10)
    )
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

- 🔌 AsyncPG
    Fast async PostgreSQL driver
    ```python
    # URL format
    postgresql+asyncpg://user:pass@host/db
    ```
    [Docs](https://magicstack.github.io/asyncpg/current/)