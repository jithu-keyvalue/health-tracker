Step 23 – Clean Architecture
========================

💭 Problem / Pain
-----------------
Code organized into layers but something's wrong.

🛠️ Tasks
--------
- Debug and fix the issues

✅ Check
--------
1. Setup services:
   - Start: `docker compose up`
   - Install dependencies: `pip install -r requirements.txt`

2. Start app:
   - Backend: `uvicorn app.main:app --reload`
   - Frontend: `cd ui && python -m http.server 8001`

3. Test the flow:
   - Add new observation
   - Check if it saves
   - Try to list data
   - Debug and fix
