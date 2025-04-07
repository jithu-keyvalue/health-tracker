📝 Notes  
--------
- 🧾 CSV (Comma-Separated Values)  
  A plain-text format to store table-like data.

- 📄 Writing to a file (basic way)  
  Use `open()` and `close()` to write manually.

  ```python
    file = open("output.txt", "w")
    file.write("some text\n")
    file.close()
  ```