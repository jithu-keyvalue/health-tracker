Step 20 – User Authentication
========================

💭 Problem / Pain
-----------------
Profile page not working after login.
Browser dev tools might help debug.

🛠️ Tasks
--------
- Debug profile page issues
- Fix authentication

✅ Check
--------
1. Setup database:
   - Reset: `docker compose down -v`  # Fresh start for provided migrations
   - Start: `docker compose up -d`
   - Run migrations: `alembic upgrade head`  # Creates users & observations tables
   - Check: `docker exec health-db psql -U healthuser -d healthdb -c "\dt"`

2. Start services:
   - Backend: `uvicorn main:app --reload`
   - Frontend: `cd ui && python -m http.server 8001`

3. Debug:
   - Try the auth flow
   - Use dev tools to investigate
   - Fix the first issue

4. Keep going:
   - Try profile again
   - Debug the new error
   - Fix the final issue
