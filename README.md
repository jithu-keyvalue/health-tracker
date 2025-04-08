Step 11 – Query Param + Swagger
===============================

💭 Problem / Pain  
-----------------
You want to say hello to users dynamically, without hardcoding a name in the backend.  
Also, is there a more convenient way to test APIs?

🛠️ Tasks  
---------
- Currently we don't get the name from query parameter in response. Fix this.

✅ Check  
--------
- Run: `uvicorn main:app --reload`
- Test in browser: `http://localhost:8000/hello?name=javed`
- Test in Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
