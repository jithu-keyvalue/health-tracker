Step 15 – Setup Postgres with Docker Compose
============================================

💭 Problem / Pain  
-----------------
CSV is great for early steps, but not reliable for real apps.  
We need a proper database to persist and query health data.

🛠️ Tasks  
---------
docker-compose.yml file got some error. We are not specifying the right file name for env it seems.

✅ Check  
--------
- Run the DB container using `docker compose up`
- Connect to the DB manually using `psql` and verify it's working:
  ```bash
  docker exec -it health-db psql -U healthuser -d healthdb
  ```
- Verify DB is live. Run inside Postgres shell: `SELECT NOW();`
