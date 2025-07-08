Step 10 – Start FastAPI
========================

💭 Problem / Pain
-----------------
So far, we've been using Python as a CLI script.
We need to turn this into a real web backend so it can talk to the outside world.

🛠️ Tasks
--------
First setup:
- Create virtual env: `python -m venv .venv`
- Activate it: `source .venv/bin/activate`
- Install deps: `pip install -r requirements.txt`

Then:
- Run server: `uvicorn main:app --reload`
- Visit http://localhost:8000/hello
- Make it greet you by name

✅ Check
--------
- Server running without errors
- Browser shows personalized greeting
- Code uses FastAPI properly
