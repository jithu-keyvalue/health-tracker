Step 17 – Store in Database
========================

💭 Problem / Pain
-----------------
Schema has incorrect column name.
Queries fail due to table name mismatch.

🛠️ Tasks
--------
- Fix schema column name and constraint
- Fix table name in queries
- Test data persistence works

✅ Check
--------
1. Create database table:
   ```bash
   docker exec -i health-db psql -U healthuser -d healthdb < schema.sql
   ```

2. Start services:
   - Start FastAPI: `uvicorn main:app --reload`
   - Start frontend: `cd ui && python3 -m http.server 8001`

3. Test data flow:
   - Add observation in UI
   - Verify it appears in list
   - Restart app and check data persists