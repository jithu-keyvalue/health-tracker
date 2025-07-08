Step 21 – Link Users and Observations
================================

💭 Problem / Pain
-----------------
Observations page shows no data after saving.
App structure has changed too.

🛠️ Tasks
--------
- Fix the startup error
- Debug the data query
- Fix the issue

✅ Check
--------
1. Setup database:
   - Start: `docker compose up -d`
   - Apply migrations: `alembic upgrade head`  # Uses provided migration scripts

2. Start services:
   - Try starting backend: `uvicorn main:app --reload`
   - Find why it fails
   - Start with correct path
   - Frontend: `cd ui && python -m http.server 8001`

3. Test the flow:
   - Login to your account
   - Add new observation
   - Data saves but doesn't show up
   - Check database content
   - Review the query logic
 
