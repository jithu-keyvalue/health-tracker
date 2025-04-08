Step 13 – Get & Validate Observations
=====================================

💭 Problem / Pain  
-----------------
You're saving health data, but can't view it.  
Also, inputs aren't being validated — a broken value can pollute the file.

🛠️ Tasks  
---------
- Nice that we are using pydantic model to validate, but the rule we've configured for hb value has an issue. It is not allowing values below 30.
- Also, are we sorting the entries by hb while getting? Let's sort it by date.

✅ Check  
--------
- Run the app: `uvicorn main:app --reload`
- Try POST-ing valid & invalid records via `/docs`
- GET `/observations` and test `skip` / `limit`
