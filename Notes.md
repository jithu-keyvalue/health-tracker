📝 Notes  
--------
- 📮 POST request:  
  Used to send data in the request **body** — good for larger or private data (not visible in URL or logs).

- 📥 Request body as dict:  
  FastAPI can auto-parse JSON into a Python `dict`.  
  Then you can use `.get()` to access values.

- 📄 `csv.writer`:  
  Used to write rows into a CSV file.  
  Open the file in append mode (`"a"`) and use `writer.writerow(...)`.

- 📁 `os.path.exists()`:  
  Checks if a file already exists.

- 📑 Constant naming:  
  File-level constants like `CSV_FILE` are written in **ALL_CAPS**.