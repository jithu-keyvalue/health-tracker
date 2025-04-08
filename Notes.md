📝 Notes  
--------
- 🔢 float()  
  Converts user input (which is always a string) into a number.

  ```python
  height = float(input("Enter your height: "))
  ```

- '#' starts a comment line

- 🔽 Indentation = Code Block  
  Python uses indentation instead of {} or begin/end.  
  Mixing tabs and spaces will break your code.

  ```python
  if x > 0:
      print("Yes")  # must be indented under if
  ```

- ⚠️ Colons (:) mean “a block is coming”  
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
