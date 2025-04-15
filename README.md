Step 22 – Celery, OpenAI & File Upload
======================================

💭 Problem / Pain  
-----------------
Manual data entry is slow and error-prone.
Users should be able to upload lab reports (PDFs), and get observations auto-extracted.

🛠️ Tasks 
--------
- Try running the app following the steps below.
- Test adding individual observations
- Test uploading file - got a 404 not found error? Check if the `POST /files/upload` route is wired properly (See `main.py` and `routes/upload.py`)


✅ Check  
--------

 - Add Open AI Apikey in .env and docker.env
 - Start DB, Redis, Celery: `sudo docker compose up`
 - Run the new migration script to add uploaded_files table: `alembic upgrade head`
 - Install new dependencies(celery, openai, redis, python-multipart): `pip install -r requirements.txt`
 - Run backend: `uvicorn app.main:app --reload`
 - Run frontend: `python -m http.server 8001`
 - Open frontend: http://localhost:8001
 - Test the UI
 
