📝 Notes
--------
- 📦 Functions
    Group code into reusable blocks.
    ```python
    def to_celsius(fahrenheit):    # lowercase_with_underscores
        return (fahrenheit - 32) * 5/9

    temp = to_celsius(98.6)    # Call function
    print(temp)                # 37.0
    ```
    [Guide](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

- 📝 Naming
    ```python
    def calculate_bmi():     # ✅ clear, lowercase
    def calculateBMI():      # ❌ not Python style
    ``` 