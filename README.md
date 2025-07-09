Step 22 – Celery, OpenAI & File Upload
======================================

💭 Problem / Pain
-----------------
Manual data entry is slow and error-prone.
File upload endpoint not reachable.

🛠️ Tasks
--------
- Debug the file upload issue
- Test the auto-extraction flow

✅ Check
--------
1. Setup services:
   - Add OpenAI API key in .env and docker.env
   - Start services: `docker compose up`
   - Apply migrations: `alembic upgrade head`
   - Install dependencies: `pip install -r requirements.txt`

2. Start app:
   - Backend: `uvicorn app.main:app --reload`
   - Frontend: `cd ui && python -m http.server 8001`

3. Test the flow:
   - Try uploading a file
   - Check the error
   - Fix the issue

4. Verify extraction:
   - Upload a lab report PDF
   - Watch the background process
   - Check extracted data
 
