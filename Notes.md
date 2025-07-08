📝 Notes
--------

- 📦 Pydantic Model
    Set rules for input fields
    ```python
    class Item(BaseModel):
        price: float = Field(..., gt=0)
        date: str = Field(pattern=r"^\d{4}-\d{2}$")
    ```
    [Docs](https://docs.pydantic.dev/latest/concepts/fields/)

- 📄 CSV Dictionary
    Read CSV as dicts
    ```python
    with open("data.csv") as f:
        rows = list(csv.DictReader(f))
    ```
    [Docs](https://docs.python.org/3/library/csv.html#csv.DictReader)

- 📋 Response Model
    Define response shape
    ```python
    @app.get("/items", response_model=List[Item])
    def get_items(skip: int = 0):
        return items[skip:skip + 10]
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/response-model/)

- 📊 Sort Lists
    Order by dict key
    ```python
    items.sort(key=lambda x: x["date"])
    ```
    [Docs](https://docs.python.org/3/howto/sorting.html)

- 🔢 List Slice
    Get page of items
    ```python
    start, limit = 0, 10
    page = items[start:start + limit]
    ```
    [Docs](https://docs.python.org/3/tutorial/introduction.html#lists)
