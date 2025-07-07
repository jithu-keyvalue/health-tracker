📝 Notes
--------
- 🌐 venv
    ```bash
    python -m venv .venv        # Create env
    source .venv/bin/activate   # Use it
    ```
    [Guide](https://docs.python.org/3/tutorial/venv.html)

- 📦 pip & requirements
    ```bash
    pip install fastapi         # Install one
    pip install -r requirements.txt  # Install all
    ```
    [Guide](https://pip.pypa.io/en/stable/user_guide/)

- 🚄 ASGI & uvicorn
    ```bash
    # ASGI: Python web standard
    uvicorn main:app --reload  # Run ASGI server
    ```
    [Guide](https://asgi.readthedocs.io/en/latest/)

- 🚀 FastAPI
    ```python
    from fastapi import FastAPI
    app = FastAPI()

    @app.get("/hello")
    def hello():
        return "Hi there"
    ```
    [Guide](https://fastapi.tiangolo.com/tutorial/first-steps/) 