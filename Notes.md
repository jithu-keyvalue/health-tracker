📝 Notes
--------

- 📤 File Upload
    Multipart form-data handling
    ```python
    # Frontend: HTML form
    <form enctype="multipart/form-data">
        <input type="file" name="file">
    </form>

    # Frontend: JavaScript
    const form = new FormData()
    form.append("file", fileInput.files[0])
    fetch("/upload", { body: form })

    # Backend: FastAPI
    @router.post("/upload")
    async def upload(
        file: UploadFile = File()  # Handles form-data field 'file'
    ):
        content = await file.read()
    ```
    File() reads from form-data field by name
    [Docs](https://fastapi.tiangolo.com/tutorial/request-files/)

- ⚙️ Celery
    Distributed task queue
    ```python
    # Initialize worker
    app = Celery(
        "worker",    # App name
        broker="redis://localhost:6379/0"  # Redis URL
    )               # protocol://host:port/db

    @app.task
    def process_file(content: str):
        result = heavy_processing(content)

    # Non-blocking call
    process_file.delay(content)
    ```
    [Docs](https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html)

- 🧠 Redis
    Message broker and cache
    ```python
    # As broker
    CELERY_BROKER_URL = "redis://redis:6379/0"

    # As cache
    redis = Redis()
    redis.set("key", "value", ex=3600)
    ```
    [Docs](https://redis.io/docs/connect/clients/python/)

- 🤖 OpenAI
    Chat completion API
    ```python
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )
    ```
    [Docs](https://platform.openai.com/docs/api-reference/chat)
