Step 16 – Connect to Postgres
========================

💭 Problem / Pain
-----------------
Database connection fails with missing configuration.
Query result also needs proper extraction.

🛠️ Tasks
--------
- Fix environment variable name
- Fix database time value extraction
- Verify connection and data

✅ Check
--------
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start services:
   - Start postgres if not running
   - Start FastAPI app

3. Test endpoint:
   - Visit /db-time
   - Should show current timestamp
   - Time should update on refresh
