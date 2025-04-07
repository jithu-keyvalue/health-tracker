📝 Notes  
--------

- 📖 `with open(...)`  
  Opens a file and ensures it gets closed **automatically**, even if an error occurs.  
  This prevents:

  - Data not being saved properly  
  - Files staying open/locked  
  - Subtle bugs from too many open files  
  
  It's cleaner and safer — no need to call `file.close()` manually.

  ```python
  with open("file.csv", "r") as f:
      for line in f:
          print(line)
  ```

  Also does not load entire file into memory, in-case you got a huge file to process.

- ⚠️ try-except  
  Used to handle errors gracefully.
  ```python
  try:
      x = int("abc")
  except ValueError:
      print("Invalid number")
  ```


- ❌ FileNotFoundError  
  Happens when you try to open a file that doesn't exist.

  ```python
  try:
      open("data.csv")
  except FileNotFoundError:
      print("File not found. Starting fresh.")
  ```

- 🔤 .strip()  
  Removes whitespace (spaces, tabs, newlines) from the start and end of a string.

  ```python
  s = "  hello\n"
  print(s.strip())  # "hello"
  ```

- 🔁 .split()  
  Splits a string into parts based on a separator (default is space).

  ```python
  "a,b".split(",")  # → ["a", "b"]
  ```

- 📊 sorted()  
  Sorts dictionary items by key (like dates).

  ```python
  sorted_dict = dict(sorted(my_dict.items()))
  ```

- ⚙️ Default function arguments  
  You can assign a default value to a parameter in a function.


  ```python
    def greet(name="Guest"):
      print(f"Hello, {name}")
  
    greet()         # Hello, Guest
    greet("Jithu")  # Hello, Jithu
  ```