📝 Notes  
--------

- 📦 Python modules:  
  Any `.py` file is a module. You can import functions from it:

  ```python
  from validation import get_date
  ```

-  🧱 Why split code?  
    - Easier to test
    - Easier to read
    - Easier to extend (add weight later, for example)

- 🧼 File naming tip:
    - Keep module names lowercase (e.g., chart.py, storage.py)
    - ✅ `validation.py`, `chart.py`  
    - ❌ `Validation.py`, `Chart.py`

- 🔍 `re.match()`  
  Regular expressions: Use the `re` module to check if a string matches a pattern.

  ```python
  import re

  re.match(r"^\d{4}-\d{2}-\d{2}$", "2024-04-07")  # ✅ match
  re.match(r"^\d{4}-\d{2}-\d{2}$", "07-04-2024")  # ❌ no match
  ```  
  
  This pattern checks if the string looks like a valid YYYY-MM-DD date.  
  📌 Tip: re.match() returns None if it doesn't match. Use it in an if condition.

  ```python
  if re.match(...):
      # valid
  else:
      # invalid
  ```