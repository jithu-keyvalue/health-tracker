Step 13 – Validate & List Data
===========================

💭 Problem / Pain
-----------------
Hemoglobin validation has wrong limits - normal values (12-17) are rejected. 
Viewing past readings is confusing because they're sorted by value 
instead of date, making it hard to track changes over time.

🛠️ Tasks
--------
- Fix validation with correct hemoglobin range
- Change sorting from hemoglobin value to date order

✅ Check
--------
- Run: `uvicorn main:app --reload`

- Test valid data:
  ```bash
  curl -X POST http://localhost:8000/observations \
    -H "Content-Type: application/json" \
    -d '{"date": "2024-03-01", "hb": 13.5}'
  ```
  Should succeed with: `{"message": "Saved"}`

- Test invalid data:
  ```bash
  curl -X POST http://localhost:8000/observations \
    -H "Content-Type: application/json" \
    -d '{"date": "2024-03-01", "hb": 50}'
  ```
  Should fail with validation error: `"Input should be less than..."`

- Test sorted data (note: quotes around URL are important):
  ```bash
  # Get first 2 entries
  curl "http://localhost:8000/observations?skip=0&limit=2"

  # Get next 2 entries
  curl "http://localhost:8000/observations?skip=2&limit=2"
  ```
  Should return entries sorted by date:
  ```json
  [
    {"date": "2024-03-01", "hb": 13.5},
    {"date": "2024-03-02", "hb": 14.0}
  ]
  ```

- Add more entries and verify:
  1. Values between 12-17 are accepted
  2. Entries are sorted by date ascending
