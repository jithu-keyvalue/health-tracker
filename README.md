Step 14 – Frontend UI + CORS
============================

💭 Problem / Pain
-----------------
Frontend can't save new observations - the API endpoint doesn't match.
Backend logs show errors for normal operations, causing false alarms.

🛠️ Tasks
--------
- Fix frontend API endpoint for saving
- Use correct log level for normal events

✅ Check
--------
1. Start servers:
   ```bash
   # Terminal 1 - Backend
   uvicorn main:app --reload

   # Terminal 2 - Frontend
   cd ui && python3 -m http.server 8001
   ```

2. Open frontend:
   - Visit: http://localhost:8001
   - Enter new observation
   - Should save successfully

3. Check logs:
   - Backend shows normal events as INFO
   - No false error messages
