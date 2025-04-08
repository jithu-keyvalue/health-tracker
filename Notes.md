📝 Notes  
--------

- 🌍 Web app basics:  
    - A **web server** is just a program that listens on a **port** (like 8000) and responds to **HTTP requests** (GET, POST, etc.).  
    - Your browser sends a GET request, the server sends back a response (like JSON or HTML).

- 🌐 What is an API?  
    - An **API (Application Programming Interface)** lets one program talk to another — usually over the internet.  
    - A web API uses **HTTP methods** (like GET, POST) and **URLs** (like `/observations`) to let you send or receive data.

  Example:

  - `GET /hello` → returns a message
  - `POST /observations` → sends data to store

  Your browser, frontend, or Postman can all talk to an API.

- 🧪 `venv` – Virtual Environment:  
  Keeps your project’s Python packages isolated from system-wide Python.

  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```

- 📦 `pip`:  
  Python’s package installer. Used to install libraries like FastAPI, Uvicorn, etc.
  ```bash
  pip install fastapi uvicorn
  ```

- 🧾 `requirements.txt`:
  A plain text file that lists the packages your project needs.
  
  ```bash
  fastapi
  uvicorn
  ```

  You install all dependencies listed in it using: `pip install -r requirements.txt`

- FastAPI: A Python framework to build APIs quickly and clearly.

- ⚡ ASGI / Uvicorn:  
  - FastAPI apps use the ASGI (Asynchronous Server Gateway Interface) standard.
  - ASGI defines how python webapps(like FastAPI apps) talk to web servers(like uvicorn).
  - Uvicorn is the ASGI server that runs your app.

- `uvicorn main:app --reload`
    - `main`: the Python file (`main.py`)
    - `app`: the FastAPI instance inside that file
    - `--reload`: auto-restart when code changes (for development)

- ⚙️ FastAPI App:  
  Create an instance of the app:

  ```python
  from fastapi import FastAPI
  app = FastAPI()
  ```

- 🔁 `@app.get("/hello")`:  
  A route that responds to GET /hello requests.  
  You can also use @app.post(...), @app.put(...), etc.
