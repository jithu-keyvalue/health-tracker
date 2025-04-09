Step 17 – Save & Fetch Observations (Raw SQL)
=============================================

💭 Problem / Pain  
-----------------
Time to start saving data in DB.  
We'll create the table manually and use raw SQL to insert and fetch data.

🛠️ Tasks  
---------
- See the `schema.sql` file. There is a command in the next section that shows how to run this so that we get our first DB table created. But ...
- Before that we better choose a better name for the column for storing haemoglobin values (use `hb`)
- Once you run the command to create table, try running the app. 
- See if you get any issues in the console(where you run Fastapi app). Fix that.

✅ Check  
--------
- Start Postgres DB (if not running): `docker compose up`
- Create table: `docker exec -i health-db psql -U healthuser -d healthdb < schema.sql`
- Run backend: `uvicorn main:app --reload`
- Serve frontend: 
  ```bash
  cd ui
  python3 -m http.server 8001
  ```
- Open frontend: http://localhost:8001
- Add an observation (date + hb)
- Confirm it shows up in the list