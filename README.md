Step 18 – SQLAlchemy ORM
===================

💭 Problem / Pain
-----------------
Data isn't being saved to database.
POST endpoint returns message instead of data.

🛠️ Tasks
--------
- Fix data persistence issue
- Define and use proper response schema

✅ Check
--------
1. Start services:
   - Start FastAPI: `uvicorn main:app --reload`
   - Start frontend: `cd ui && python3 -m http.server 8001`

2. Test saving:
   - List current observations
   - Add new observation
   - List again - new data not there
   - Fix the issue
   - Try again - new data should appear
