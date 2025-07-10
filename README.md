Step 24 – App Infrastructure
========================

💭 Problem / Pain
-----------------
Added settings, middleware and versioning.
Rate limiting is too strict - can't use app properly.

🛠️ Tasks
--------
- Debug the rate limiting issue
- Adjust the limits to be usable

✅ Check
--------
1. Setup:
   - Start: `docker compose up`
   - Install: `pip install -r requirements.txt`

2. Start app:
   - Backend: `uvicorn app.main:app --reload`
   - Frontend: `cd ui && python -m http.server 8001`

3. Test the flow:
   - Try using the app
   - Notice rate limits
   - Fix the issue
 

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
1. App starts without errors after async migration
2. Users page loads quickly (single query)
3. Observation list shows 10 items per page
 
