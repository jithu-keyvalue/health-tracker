📝 Notes
--------

## ⚡ Python Async Architecture

**Single Thread, Dual Execution**
```python
# SAME PROCESS, SAME THREAD - two execution modes:

# 1. Regular Python (sync) - blocks thread
def sync_function():
    time.sleep(1)    # Thread waits/blocks
    return "done"

# 2. Event Loop (async) - cooperative scheduling  
async def async_function():
    await asyncio.sleep(1)  # Event loop switches to other tasks
    return "done"
```

**What Handles What**
```python
async def handler():
    x = 2 + 2           # Regular Python interpreter
    print("hello")      # Regular Python interpreter
    await db.execute()  # Event loop schedules this
    time.sleep(1)       # Python interpreter BLOCKS everything
```

**The Problem: Blocking vs Non-blocking**
```python
# ❌ Blocks entire server (all users wait)
async def bad_handler():
    time.sleep(5)       # Freezes event loop + all requests

# ✅ Only pauses this request (other users unaffected)
async def good_handler():
    await asyncio.sleep(5)  # Event loop handles other requests
```

## 🗄️ SQLAlchemy Async Basics

**Core Setup**
```python
# Engine = connection pool manager (SQLAlchemy → asyncpg → PostgreSQL)
engine = create_async_engine("postgresql+asyncpg://...")

# AsyncSession = database work session (like login session - remembers your actions)
AsyncSessionLocal = async_sessionmaker(engine)
```

**Session Management** - Always use context manager
```python
# ✅ Do this
async with AsyncSessionLocal() as db:
    await db.commit()

# ❌ Don't do this
db = AsyncSessionLocal()
await db.close()  # Easy to forget, causes leaks
```

**Query Patterns**
```python
# Single result
stmt = select(User).where(User.id == 1)
result = await db.execute(stmt)
user = result.scalar_one_or_none()

# Multiple results  
stmt = select(User)
result = await db.execute(stmt)
users = result.scalars().all()
```

**The await Rule** - Everything DB-related needs `await`
```python
await db.execute(stmt)     # ✅ Query execution
await db.commit()          # ✅ Save changes
await db.refresh(obj)      # ✅ Reload from DB

# ❌ Missing await = silent failures
db.commit()  # Returns coroutine, doesn't save
```

**Transaction Handling** - Always rollback on errors
```python
try:
    db.add(user)
    await db.commit()
except Exception:
    await db.rollback()  # Always rollback - context manager auto-starts transaction
    raise
```

## 🔄 Asyncio Context Management

**Event Loop** - Invisible manager that runs your async code
```python
# You don't interact with it directly - just use async/await
async def handler():
    await db.execute(stmt)  # Event loop handles this automatically
```

**Context Boundaries**
```python
# Sync context (CLI scripts, non-async functions)
def sync_function():
    result = asyncio.run(async_function())  # Creates new event loop

# Async context (FastAPI handlers, async functions)
async def async_function():
    result = await other_async_function()  # Uses existing event loop
```

**Background Tasks** - Celery workers run in separate processes
```python
@celery_app.task  # Celery is sync-only, runs in worker process
def process_data(data):
    asyncio.run(_process_async(data))  # Creates event loop in worker

async def _process_async(data):
    async with AsyncSessionLocal() as db:
        await _business_logic(db, data)
```

## 🔗 FastAPI Integration

**Dependency Injection**
```python
async def get_db():
    async with AsyncSessionLocal() as db:
        yield db

@router.get("/users")
async def get_users(db: AsyncSession = Depends(get_db)):
    return (await db.execute(select(User))).scalars().all()
```

## 📋 Pydantic + ORM

**model_validate()** - Converts data into Pydantic model
```python
class UserOut(BaseModel):
    name: str

# Validates and creates model from dict
user_model = UserOut.model_validate({"name": "John"})
```

**Convert SQLAlchemy objects to Pydantic models**
```python
class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)  # Enable ORM mode
    name: str

# Problem: Pydantic expects dict by default
UserOut.model_validate({"name": "John"})  # ✅ Works
UserOut.model_validate(user_obj)          # ❌ ValidationError

# Solution: from_attributes=True reads object attributes
UserOut.model_validate(user_obj)          # ✅ Now works
```

## 🚫 Common Mistakes

**SQLAlchemy Errors**
```python
# ❌ Missing await = AttributeError  
result = db.execute(stmt)  # Returns coroutine
result.scalars()           # Fails
```

**Asyncio Errors**
```python
# ❌ Event loop already running (inside FastAPI handler)
async def handler():
    asyncio.run(async_func())  # Error: can't nest event loops

# ❌ Blocking calls freeze the entire server
async def handler():
    time.sleep(1)  # FREEZES all requests for 1 second
    # Fix: await asyncio.sleep(1)  # Only pauses this handler
```

## 📚 Migration Guide

**Sync → Async Patterns**
```python
# Old (sync)                 # New (async)
db.query(User).all()    →    await db.execute(select(User))
db.commit()             →    await db.commit()
Session()               →    async with AsyncSessionLocal()
function()              →    asyncio.run(async_function())
```

[SQLAlchemy Docs](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) • [Asyncio Docs](https://docs.python.org/3/library/asyncio.html)