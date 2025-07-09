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
 
