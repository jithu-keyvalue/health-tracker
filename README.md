Step 10 – Start FastAPI
========================

💭 Problem / Pain  
-----------------
So far, we’ve been using Python as a CLI script.
We need to turn this into a real web backend so it can talk to the outside world.

🛠️ Tasks  
---------
- Create a virtual environment: `python3 -m venv .venv`
- Activate the env: `source .venv/bin/activate`
- Install FastAPI, Uvicorn: `pip install -r requirements.txt`
- Make GET /hello endpoint in `main.py` say hello to you (have your name in API response)

✅ Check  
--------
- Run the server:  
  `uvicorn main:app --reload`  
- Visit: [http://localhost:8000/hello](http://localhost:8000/hello)  
- You should see: `"Hello <your name>"`
