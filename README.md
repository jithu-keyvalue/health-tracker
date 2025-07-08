Step 19 – Database Migrations
=========================

💭 Problem / Pain
-----------------
Tables created directly with create_all() are hard to change.
Need a way to track and manage database schema changes.

🛠️ Tasks
--------
- Set up Alembic configuration
- Create first migration
- Apply migration to database

✅ Check
--------
1. Clean start:
   - Remove old DB: `docker compose down -v`
   - Start fresh: `docker compose up -d`

2. Prepare migrations:
   - Create directory: `mkdir -p alembic/versions`
   - Generate: `alembic revision --autogenerate -m "observations"`
   - Check generated file in alembic/versions

3. Apply changes:
   - Run: `alembic upgrade head`
   - Start FastAPI: `uvicorn main:app --reload`
   - Add observation
   - Verify table exists with correct schema
  