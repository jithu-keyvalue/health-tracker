📝 Notes  
--------

- 📄 CREATE TABLE  
  SQL command to define your table structure.

- 🔁 CREATE TABLE IF NOT EXISTS  
  Only creates the table if it doesn’t already exist — avoids errors on rerun.

- 🔢 SERIAL  
  Auto-incrementing integer — useful for IDs (id SERIAL PRIMARY KEY).

- 📝 INSERT INTO (...) VALUES (...)  
  Used to add new rows to the table.

  ```sql
  INSERT INTO observations (date, hb) VALUES ('2024-04-10', 13.5);
  ```

- 📥 SELECT ... ORDER BY  
  Used to fetch rows, sorted by a column.

  ```sql
  SELECT date, hb FROM observations ORDER BY date;
  ```

- 📑 OFFSET + LIMIT  
  Used for pagination — skips and limits results.

  ```sql
  SELECT ... ORDER BY date OFFSET 0 LIMIT 10;
  ```

- 📦 cur.fetchone()  
  Fetches a single row from the SELECT result. Use when expecting just one row.

- 📦 cur.fetchall()  
  Fetches all rows as a list of tuples.

- 🧾 conn.commit()  
  Saves any changes made (e.g. inserts).  
  Without this, the changes are discarded when the connection closes.