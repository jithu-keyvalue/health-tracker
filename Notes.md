📝 Notes  
--------
- ➰ Looping through a dictionary  
  Use `.items()` to get both key and value in a loop:

  ```python
  for key, value in some_dict.items():
      print(key, value)
  ```

- 🔁 String multiplication  
Repeat a character using *:
  ```python
    print("▓" * 10)  # ▓▓▓▓▓▓▓▓▓▓
  ```

- 🧾 f-string formatting  
  You can control width and alignment in f-strings:
  ```python
    print(f"{label} | {bar:<20} {value}")
  ```

  :<20 → left-align to 20 characters (helps make the chart neat)