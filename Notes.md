📝 Notes  
--------

- 📄 Create Table
    Define table structure
    ```sql
    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL CHECK (price > 0)
    );
    ```
    [Docs](https://www.postgresql.org/docs/current/sql-createtable.html)

    Key concepts:
    - SERIAL: Auto-incrementing ID
    - PRIMARY KEY: Unique identifier
    - CHECK: Validate values
    - IF NOT EXISTS: Skip if table exists

- 📝 Insert Data
    Add new rows
    ```sql
    INSERT INTO items (name, price)
    VALUES ('item1', 10.5);
    ```
    [Docs](https://www.postgresql.org/docs/current/sql-insert.html)

- 📥 Query Data
    Fetch and sort rows
    ```sql
    -- Basic select
    SELECT * FROM items;

    -- With pagination
    SELECT * FROM items
    ORDER BY name
    OFFSET 0 LIMIT 10;
    ```
    [Docs](https://www.postgresql.org/docs/current/sql-select.html)

- 📦 Result Fetching
    Get query results
    ```python
    row = cur.fetchone()     # Get one row
    rows = cur.fetchall()    # Get all rows
    ```
    [Docs](https://www.psycopg.org/docs/cursor.html)

- 🔄 Transaction
    Save or discard changes
    ```python
    try:
        cur.execute("INSERT ...")
        conn.commit()      # Save changes
    except:
        conn.rollback()    # Discard on error
    finally:
        cur.close()       # Clean up
        conn.close()
    ```
    [Docs](https://www.postgresql.org/docs/current/tutorial-transactions.html)