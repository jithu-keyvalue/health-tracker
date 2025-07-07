📝 Notes
--------
- 🔍 if-elif-else
    Check conditions in sequence.
    ```python
    if score > 90:
        print("A")         # First check
    elif score > 80:       # Only if first was False
        print("B")
    else:                  # If none matched
        print("C")
    ```
    [Guide](https://docs.python.org/3/tutorial/controlflow.html)

- 🔗 and
    Combine conditions - both must be True.
    ```python
    if age > 18 and score > 90:
        print("Adult with high score")
    ``` 