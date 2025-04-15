📝 Notes
--------

- 📤 File Upload (FastAPI)  
  Endpoint accepts UploadFile using multipart/form-data.

  ```python
  @router.post("/upload")
  async def upload_file(file: UploadFile = File(...)):
  ```

  In frontend:

    ```javascript
    const form = new FormData();
    form.append("file", selectedFile);

    fetch("/upload", {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
      body: form,
    });
    ````

  FastAPI automatically parses multipart requests and makes file available as UploadFile.

- 🔁 Duplicate File Check  
  We compute a SHA256 hash of the file content:

  ```python
  file_hash = hashlib.sha256(content).hexdigest()
  ```

  This hash is unique to the file contents, so if a user uploads the same file again, we detect it and skip reprocessing.

- ⚙️ Celery – Background Tasks  
  Celery is a distributed task queue that lets you offload heavy/background jobs like file parsing.
    - Uses Redis as the message broker
    - Workers run separately and listen for jobs

  A message broker is a system that acts like a middleman between FastAPI and Celery workers.
  - FastAPI pushes a job (like process_file) into the broker
  - Celery worker pulls the job from broker and processes it
  
  Setup:

  ```python
  from celery import Celery
  celery_app = Celery("myapp", broker="redis://redis:6379/0")
  ```

  Mark a task:

  ```python
  @celery_app.task
  def process_uploaded_file(file_hash, content, user_id):
    ...
  ```

  Call the task from FastAPI:
  ```python
  process_uploaded_file.delay(file_hash, text, user_id)
  ```

  .delay() is a shortcut for queuing a background task.

- 🧠 Redis  
  In our project, Redis is used as the broker to queue Celery jobs.

  Usage as a cache:

  ```python
  import redis

  r = redis.Redis(host="localhost", port=6379, db=0)

  r.set("mykey", "hello")
  print(r.get("mykey")) 
  ```



- 📄 PyPDF2 – Reading PDF in Python  
  PyPDF2 is a library used to read and extract text from PDF files.
 
- 🧬 Data Migration via Alembic  
  Alembic lets us migrate live data using Python code inside the migration script. This avoids data loss while changing schemas.

- 🤖 OpenAI Chat Completion API  
  We use OpenAI's gpt-3.5-turbo to extract data like Hb, Cholesterol, etc. from PDF.

  ```python
  from openai import OpenAI
  client = OpenAI(api_key=...)

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
  )
  ```
  
  messages: a list of {role: ..., content: ...}

  role: user (your input), assistant (AI's reply)
