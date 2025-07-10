📝 Notes
--------

- 🔄 Async Database
    SQLAlchemy 2.0 with asyncpg brings async/await to your DB
    ```python
    # Engine setup
    engine = create_async_engine("postgresql+asyncpg://")
    
    # Session usage
    async with AsyncSession(engine) as db:
        stmt = select(Item)
        items = await db.scalars(stmt)
    
    # Route pattern
    @router.get("/items")
    async def list_items(db: AsyncSession):
        return await db.scalars(select(Item))
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)

    ✅/❌ Common Patterns
    ```python
    # ✅ Use context manager
    async with AsyncSession() as db:
        await db.execute(stmt)
    
    # ❌ Avoid raw execute
    items = await db.execute(stmt)
    # ✅ Use scalars/scalar
    items = await db.scalars(stmt)
    
    # ❌ N+1 queries
    users = await db.scalars(select(User))
    for user in users:
        await get_items(user.id)  
    # ✅ Use relationship loading
    stmt = select(User).options(selectinload(User.items))
    ```

    🎯 Exercise 1: Fix Query Performance
    ```python
    @router.get("/users-items")
    async def get_users(db: AsyncSession):
        # Current: Makes N+1 queries
        stmt = select(User)
        users = await db.scalars(stmt)
        
        return [{
            "name": u.name,
            "items": await get_items(u.id)
        } for u in users]
    ```
    Task: Optimize to use a single query
    Hint: Research selectinload() or joinedload()

    🎯 Exercise 2: Add Pagination
    ```python
    @router.get("/items/list")
    async def list_items(db: AsyncSession):
        # Current: Returns all items
        stmt = select(Item).order_by(Item.id)
        return await db.scalars(stmt)
    ```
    Task: Add offset pagination (10 per page)
    Must return:
    - items: List[Item]
    - total: int
    - has_next: bool
    Hint: Use func.count() with limit/offset