Step 14 – Frontend UI + CORS
============================

💭 Problem / Pain  
-----------------
Your API works — but users can’t interact with it visually.  
Also, browsers block frontend → backend calls unless CORS is allowed.

🛠️ Tasks  
---------
- Unable to add new observations from frontend. Is everything alright with the POST API call?
- Logging is fine, but why are we using "error" log level for a simple info?

✅ Check  
--------

- In one terminal (FastAPI backend): `uvicorn main:app --reload`
- In another terminal (Frontend):
    ```bash
    cd ui
    python3 -m http.server 8001
    ```
- Open: http://localhost:8001
- Should see existing entries
- Submit a new entry → it should appear in the list
