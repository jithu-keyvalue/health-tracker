Step 25 - Async Database
===========================

💭 Problem
-----
Multiple pages are broken! After switching to async SQLAlchemy, 
both the profile page and observations list have different async-related errors.

Something went wrong during the async migration - you'll need to debug 
and fix the async/await usage in the API endpoints.

🛠️ Tasks
-----
- [ ] Fix the async issues in the API endpoints

✅ Check
-----
1. Setup:
    - Install: `pip install -r requirements.txt`
    - Start services: `docker compose up -d`
    - Run migrations: `alembic upgrade head`

2. Run App:
    - Backend: `uvicorn app.main:app --reload`
    - Frontend: `cd ui && python -m http.server 8001`

3. Test the Fix:
    - Login with existing account
    - Visit profile page (should work)
    - Visit home page - observations should load
    - Check server logs for async-related errors

4. Success:
    - Profile page loads correctly
    - Home page shows user's observations correctly
    - No async-related errors in logs
 
