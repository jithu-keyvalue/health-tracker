Step 23 – Services, Repositories & Global exception handler
===========================================================

💭 Problem / Pain  
-----------------
As apps grow, mixing routing, business logic, and DB code gets messy.
We also need better error handling.

🛠️ Tasks 
--------
- Now we have split code into services, repositories, etc. 
- But while doing that, an error has crept in - observations list is empty. Debug and fix!

✅ Check  
--------

 - Add Open AI Apikey in .env and docker.env
 - Start DB, Redis, Celery: `sudo docker compose up`
 - Run backend: `uvicorn app.main:app --reload`
 - Run frontend: `python -m http.server 8001`
 - Open frontend: http://localhost:8001
 - Test the UI
 
