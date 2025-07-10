Step 25 - Async Database Performance
===========================

💭 Problem
-----
The health tracker is getting slow as more users upload lab reports. 
Database queries are blocking each other and the app feels sluggish.
Users also report seeing timeouts when viewing large lists of records.

🛠️ Tasks
-----
- [ ] Switch to async database with SQLAlchemy 2.0
- [ ] Fix the N+1 query in users/observations page
- [ ] Add pagination to observation list

✅ Check
-----
1. Setup:
    - Install requirements: `pip install -r requirements.txt`
    - Start database: `docker compose up -d`
    - Run migrations: `alembic upgrade head`

2. Run App:
    - Start backend: `uvicorn app.main:app --reload`
    - Start frontend: `cd ui && python -m http.server 8001`

3. Verify:
    - App starts without SQLAlchemy warnings
    - Users page loads without errors
    - Observation list shows paginated results
 
