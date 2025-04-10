Step 19 – Alembic Migrations
============================

💭 Problem / Pain  
-----------------
We’ve been using `Base.metadata.create_all()` to create tables, but it’s not ideal for managing schema changes over time.  
Alembic provides an automated way to handle DB schema migrations, keeping track of changes.

🛠️ Tasks  
---------
Learn how to generate migrations, and run those migrations by following the step below

✅ Check  
--------
Preparing:
- Remove DB: `sudo docker compose down -v` (because we had already created the observations table manually in the previous step)
- Create DB: `sudo docker compose up`
- Install new dependency (alembic): `pip install -r requirements.txt`
- Create a folder `versions` inside alembic folder

Creating & running migrations:
- Generate migration: `alembic revision --autogenerate -m "Create observations table"` (see if you have a new python module generated in `alembic/versions`)
- Apply migration: `alembic upgrade head`

Testing app:
- Run backend: `uvicorn main:app --reload`
- Run frontend: `python -m http.server 8001`
- Open frontend: http://localhost:8001
- Test adding an observation
- Test getting observations
  