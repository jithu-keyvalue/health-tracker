📝 Notes
--------

- 🔍 Query Parameters
    URL data after ? mark
    ```python
    @app.get("/items")
    def get_item(color: str):  # ?color=blue
        return {"color": color}
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/query-params/)

- 📊 JSON Response
    Always return JSON objects
    ```python
    return {"id": 1, "name": "item"}
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/response-model/)

- 📘 Swagger UI
    Auto-generated API testing
    ```
    /docs    - Try endpoints
    /redoc   - Read API docs
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/metadata/)

- 🧾 OpenAPI:  
  An industry standard that defines what your API can do (routes, inputs, outputs).  
  FastAPI generates it automatically using type hints.

- 🧪 Swagger UI:  
  A browser-based UI to explore and test your API.  
  Open http://localhost:8000/docs  
  No Postman needed — click, fill, test.  

- 🔤 Type Hints (like `name: str`):  
  Type hints tell Python (and FastAPI) what kind of value is expected.

  ```python
  def greet(name: str):
      ...
  ```

  Used by FastAPI to:
    - ✅ Validate inputs automatically  
      → Wrong type? You get a `422 Unprocessable Entity`  
    - 🧾 Generate docs and input fields in Swagger  
    - 💡 Improve editor suggestions and catch bugs early