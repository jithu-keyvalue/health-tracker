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
 
