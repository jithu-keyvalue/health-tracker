📝 Notes  
--------

- 🐘 psycopg2  
  A Python library to connect and interact with a Postgres DB.

  ```python
  import psycopg2
  conn = psycopg2.connect(...)
  ```

- 🔌 Database Connection  
  Like opening a live session with the database — needed to send queries.

- 🧭 Cursor  
  Once connected, the cursor is your "command prompt" inside the DB — used to run SQL and fetch results.

  ```python
  cur = conn.cursor()
  cur.execute("SELECT NOW()")
  result = cur.fetchone()
  ```

- 📥 cur.fetchone()   
  Fetches **a single row** from the result of a SQL query.
    - Returns a tuple: e.g. `("2024-04-10 17:42:01.123456",)`
    - Use when expecting **one result only** (like `SELECT NOW()`)

- 🚪 cursor.close()  
  Tells Postgres you're done running queries.
  Frees up memory, locks, and threads on the DB server.

- 🔒 connection.close()  
  Ends the session with the database.
  Important: avoids exhausting the DB’s limited connection pool.

- 🌍 os.getenv(...)  
  Used to fetch environment variable values in Python — clean way to load secrets/config.

  ```python
  os.getenv("DB_PASSWORD")
  ```

- 🗂️ .env vs docker.env  
  - .env - used by FastAPI app	(Python reads this via dotenv)
  - docker.env - used by Docker Compose	(Used to configure containers. e.g. Postgres image)