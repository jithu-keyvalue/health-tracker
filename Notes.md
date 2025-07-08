📝 Notes
--------

- 📮 POST Request
    Send data in request body
    ```python
    @app.post("/items")
    def add_item(data: dict):
        return {"id": 1}
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/body/)

- 📄 CSV Writer
    Write rows to CSV file
    ```python
    with open("data.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name"])
    ```
    [Docs](https://docs.python.org/3/library/csv.html)

- 📁 File Operations
    Check and create files
    ```python
    if not os.path.exists("data.csv"):
        open("data.csv", "a").close()
    ```
    [Docs](https://docs.python.org/3/library/os.path.html)