Step 21 – Link User and Observations, Home Page
===============================================

💭 Problem / Pain  
-----------------
We need to link the **`User`** and **`Observation`** tables and display observations tied to the currently logged-in user.  

🛠️ Tasks 
--------
- Run the new migration script to add foreign key in Observation table: `alembic upgrade head`
- When you run the app, there is an issue with listing entries. The API to get observations isn't working properly. Please fix this.


✅ Check  
--------

Test app:
 - Run backend: `uvicorn app.main:app --reload`
 - Run frontend: `python -m http.server 8001`
 - Open frontend: http://localhost:8001
 - Test the UI
 
