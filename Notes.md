📝 Notes
--------
- 🔄 Dictionary Loop
    Get both key and value in each iteration.
    ```python
    data = {"a": 1, "b": 2}
    for key, val in data.items():
        print(key, val)    # a 1, then b 2
    ```
    [Guide](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

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