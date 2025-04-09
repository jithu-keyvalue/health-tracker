Step 16 – Connect FastAPI to Postgres (Raw)
===========================================

💭 Problem / Pain  
-----------------
The database is running, but your app isn’t talking to it yet.  
Let’s connect to Postgres and fetch something simple — like the current DB time.

🛠️ Tasks  
---------
- DB time API works, but incorrect time value. Can you see how to get the correct time value?   
[hint: use print() to see what values any intereting variables have during request processing]

✅ Check  
--------
- Install new deps (psycopg2-binary, python-dotenv): `pip install -r requirements.txt`
- Start Postgres container (if not already running): `docker compose up`
- Start FastAPI app: `uvicorn main:app --reload`
- Visit: `http://localhost:8000/db-time`
- You should see the current timestamp returned from Postgres
