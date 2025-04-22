Step 24 – Settings, Middleware, health check, API versioning
============================================================

💭 Problem / Pain  
-----------------
Project structure is getting more complex. We need:
- Centralized config handling
- Basic health monitoring
- Middleware for useful request logging
- Versioned API setup for future upgrades

🛠️ Tasks 
--------
- Check the logs, the time taken by each request as per logs is too much?

✅ Check  
--------

 - Add Open AI Apikey in .env and docker.env
 - Install new dependency: `pip install -r requirements.txt`
 - Start DB, Redis, Celery: `sudo docker compose up`
 - Run backend: `uvicorn app.main:app --reload`
 - Run frontend: `python -m http.server 8001`
 - Open frontend: http://localhost:8001
 - Test app
 
