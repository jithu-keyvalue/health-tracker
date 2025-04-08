📝 Notes  
--------

- ❓ Query Parameters:  
  Extra values passed in the URL after `?`. Common for filters, inputs, etc.

  ```url
  /greet?name=Alice
  ```

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