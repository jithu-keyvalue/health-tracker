Step 11 – Query Parameters
=======================

💭 Problem / Pain
-----------------
API greets with hardcoded text. No way to test endpoints easily.

🛠️ Tasks
--------
- Use name from URL query
- Return JSON response
- Try Swagger UI

✅ Check
--------
- Run: `uvicorn main:app --reload`
- Test: http://localhost:8000/hello?name=Alice
- See: {"message": "Hello, Alice!"}
- Open: http://localhost:8000/docs
