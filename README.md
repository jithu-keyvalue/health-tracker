Step 20 – User Table, Signup, Login, and Profile
================================================

💭 Problem / Pain  
-----------------
We need to store users securely and authenticate them.  
This step introduces the **users table**, **signup**, **login**, and **user profile**.

🛠️ Tasks 
--------
- Follow the steps below to create tables & Sign up
- Then you would be able to login
- But the next call to get the profile info fails. Check whether we are setting the token properly in `index.html` when user logs in.

✅ Check  
--------
Preparing:
 - Remove DB: `sudo docker compose down -v` (because going forward this training repo will provide generated scripts - we already learnt how to generate migrations in the last step. So we need to start fresh to make sure revision numbers match for all of us)
 - Create DB: `sudo docker compose up`
 - Install new dependency (alembic): `pip install -r requirements.txt`


Create users, observations tables:
 - Apply migrations: `alembic upgrade head`
(2 migrations scripts already available in alembic/versions)

Test app:
 - Run backend: `uvicorn main:app --reload`
 - Run frontend: `python -m http.server 8001`
 - Open frontend: http://localhost:8001
 - Signup first
 - Try login
 - Verify you can see profile details
 
