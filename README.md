Step 09 – Input Validation & Modules
====================================

💭 Problem / Pain  
-----------------
The program is growing — it's hard to read, test, or extend when everything is in one file.  
Also, inputs can be invalid or messy, leading to crashes or bad data.

🛠️ Tasks  
---------
- There is something wrong in `main.py` around how we use `print_chart`. Fix it.

✅ Check  
--------
- Run `python main.py`
- Try invalid name/date/Hb — it should handle and re-prompt
- Check the file: `<name>.csv` gets created with valid data
- Code is organized across smaller, focused files
