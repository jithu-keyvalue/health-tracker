📝 Notes
--------
- 📖 Reading Files
    ```python
    with open("data.txt") as file:
        for line in file:           # Read line by line
            print(line.strip())     # Remove extra \n
    ```
    [Guide](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

- 🛡️ Error Handling
    ```python
    try:
        file = open("data.txt")     # This might fail
    except FileNotFoundError:
        print("No file yet")        # Handle gracefully
    ```
    [Guide](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) 