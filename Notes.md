📝 Notes
--------

- 🐘 Postgres Connect
    Connect to database server
    ```python
    conn = psycopg2.connect(
        host="localhost",
        dbname="mydb",
        user="admin"
    )
    ```
    [Docs](https://www.psycopg.org/docs/module.html)

- 🔍 Execute Query
    Run SQL and get results
    ```python
    cur = conn.cursor()
    cur.execute("SELECT id FROM users")
    row = cur.fetchone()  # Returns tuple
    print(row[0])  # Get first column
    ```
    [Docs](https://www.psycopg.org/docs/cursor.html)

- 🧹 Clean Up
    Close database resources
    ```python
    cur.close()    # Close cursor first
    conn.close()   # Then connection
    ```
    [Docs](https://www.psycopg.org/docs/connection.html#connection.close)

- 🔐 Environment
    Load config from files
    ```python
    # App reads .env
    from dotenv import load_dotenv
    load_dotenv()
    password = os.getenv("DB_PASS")

    # Docker reads docker.env
    services:
      db:
        env_file: docker.env
    ```
    [Docs](https://pypi.org/project/python-dotenv/)