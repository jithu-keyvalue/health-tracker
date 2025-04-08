Step 12 – POST Observation (Save to CSV)
========================================

💭 Problem / Pain  
-----------------
You can’t track health data unless it's stored somewhere.  
Let's enter data in frontend and save it in backend.

🛠️ Tasks  
---------
- Somehow the data is not getting saved in the csv in the proper way. Fix this.

✅ Check  
--------
- Run the app: `uvicorn main:app --reload`
- Open `/docs`, post this:

  ```json
  {
    "date": "2024-04-10",
    "hb": 13.5
  }
  ```
- Check that observations.csv is created and contains correct data