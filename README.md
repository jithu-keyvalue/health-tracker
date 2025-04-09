Step 18 – Use SQLAlchemy ORM
============================

💭 Problem / Pain  
-----------------
Raw SQL works but it’s low-level, repetitive, and hard to scale.  

We need a cleaner, model-driven way to interact with the DB.

🛠️ Tasks  
---------
- Install the dependency and run the app, things look fine. But ...
- Are observations actually getting saved? check the POST endpoint once again - the db calls are fine?

✅ Check  
--------
- Install new dependency(sqlalchemy): `pip install -r requirements.txt`
- Run backend: `uvicorn main:app --reload`
- Run frontend: `python -m http.server 8001`
- Open frontend: http://localhost:8001
- Test getting observations → under the hood using ORM
- Test adding an observation → it should be saved in DB via ORM
