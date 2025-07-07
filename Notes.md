📝 Notes  
--------
- 🔢 Converting Input
    ```python
    age = float(input("Age: "))     # ✅ Clear conversion
    x = input("Age: "); float(x)    # ❌ Confusing steps
    ```
    [Docs](https://docs.python.org/3/library/functions.html#float)

- 🔍 Conditions
    ```python
    if age >= 18:                   # ✅ Clear condition
        print("Adult")
    if (age >= 18) == True:         # ❌ Redundant check
        print("Adult")
    ```
    [Guide](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

- 📏 Code Blocks
    ```python
    if value < 10:
        print("Low")                # ✅ Consistent indent
        print("Check again")

    if value < 10:
       print("Low")                 # ❌ Mixed indents
         print("Check again")
    ```
    [Style Guide](https://peps.python.org/pep-0008/#indentation)

- 💡 Comments
    ```python
    # Age categories:               # ✅ Helpful context
    if age < 18:
    
    if age < 18:  # check adult    # ❌ Obvious comment
    ```

- '#' starts a comment line

- 🔽 Indentation = Code Block  
  Python uses indentation instead of {} or begin/end.  
  Mixing tabs and spaces will break your code.

  ```python
  if x > 0:
      print("Yes")  # must be indented under if
  ```

- ⚠️ Colons (:) mean "a block is coming"  
  Every if, while, for, def, etc. ends with a colon.

  ```python
  def greet():
      print("hi")  # ← this line is inside the function
  ```

- 🤔 if-elif-else  
  Use conditional logic to branch based on values.

  ```python
  if condition:
      ...
  elif other_condition:
      ...
  else:
      ...
  ```
