Step 15 – Setup Postgres DB
========================

💭 Problem / Pain
-----------------
CSV files can't handle multiple users or concurrent access.
Database container fails to start - can't find configuration.

🛠️ Tasks
--------
- Fix database configuration issue
- Start database container
- Verify connection works

✅ Check
--------
1. Start database:
   - Use docker compose to start in background

2. Verify it's running:
   ```bash
   docker ps
   ```

3. Test connection:
   - Connect to postgres inside container
   - Run a test query (check current time)
   - Exit psql shell
