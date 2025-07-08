Step 12 – Save Observations
========================

💭 Problem / Pain
-----------------
Health data needs to be stored for tracking.
CSV file shows wrong data order.

🛠️ Tasks
--------
- Post new observation via /docs
- Check CSV content
- Fix data saving order

✅ Check
--------
- Run: `uvicorn main:app --reload`
- Post: /observations
  ```json
  {
    "date": "2024-04-10",
    "hb": 13.5
  }
  ```
- CSV: date and hb in correct columns