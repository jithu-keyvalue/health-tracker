📝 Notes  
--------

- 📦 Pydantic Model  
  Used to define the structure and validation rules for request/response.

  ```python
  from pydantic import BaseModel, Field

  class Observation(BaseModel):
      date: str
      hb: float
  ```

- Use Field() to add extra rules:  

  ```python
  date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$")
  hb: float = Field(..., gt=0)
  ```


- 🔁 CSV DictReader  
  Reads each row as a dictionary, with keys from the header row.

- 📊 Sorting with sort()  
  Sorts a list of dicts by a field (like date string).

  ```python
  data.sort(key=lambda r: r["date"])
  ```

- 🧪 Response Model (List[])  
  You can return a list of models like this:

  ```python
  from typing import List

  @app.get("/observations", response_model=List[Observation])
  ```
  
  This tells FastAPI what the output should look like.
  - converts raw data into typed, validated objects  
  - powers Swagger docs

- 🎛️ Pagination with Query Params  
  skip and limit are passed like this: `/observations?skip=2&limit=5`
  
  FastAPI auto-converts them to integers: `def get(skip: int = 0, limit: int = 10):`

- 🔢 Slicing with skip & limit - used for pagination:
  ```python
  data = ["a", "b", "c", "d", "e"]
  data[1 : 1 + 2]  # → ['b', 'c']
  ```
