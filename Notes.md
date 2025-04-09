📝 Notes  
--------

- 🧱 SQLAlchemy ORM  
  Lets you define tables as Python classes, and rows as Python objects.  
  No raw SQL needed.

- 🤝 Why ORM?
  - Cleaner code (no manual SQL)
  -  Reusable models
  - Safer queries (built-in escaping)
  - Easier to test, extend, and refactor

- 🏗️ ORM Model Definition
  ```python
  class Observation(Base):
      __tablename__ = "observations"
      id = Column(Integer, primary_key=True)
      date = Column(Date, nullable=False)
      hb = Column(Float, nullable=False)
  ```
  - Column(...): defines a DB column

  - Integer, Date, Float: column types

  - nullable=False: column is required (NOT NULL)

- 🛡️ CheckConstraint
  Used to enforce rules in DB (e.g., hb must be > 0)

- 🧰 Session & DB Setup

  ```python
  engine = create_engine(DB_URL)
  SessionLocal = sessionmaker(bind=engine)
  Base = declarative_base()
  ```

  - create_engine(...): connects to Postgres
  - SessionLocal(): creates a session for DB operations
  - Base: parent for all ORM models

- 🧪 Session Usage
  ```python
  db = SessionLocal()
  db.add(obj)
  db.commit()
  db.query(Model).filter(...).all()
  ```

  -  add(...): stage a new row
  - commit(): write it to DB
  - query(...): fetch rows using ORM
  - Always close session after use

- 🚦 Base.metadata.create_all(engine)  
  Creates all tables defined by models.
  - ⚠️ Dev only — we'll replace this with migrations.

- 🧬 Dependency Injection (DI) 
  Dependency Injection is a way to automatically provide objects (like DB sessions, config, current user, etc.) to your functions without you manually creating or wiring them each time.

  ```python
  def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
  ```
  - Used with `Depends(get_db)` in FastAPI
  - The yield gives you a DB session for the request
  - After response is sent, finally closes the session
  - This pattern avoids leaks and ensures clean resource use
  - Easier testing (swap out dependencies)


🔐 How ORM Protects Against SQL Injection  
-----------------------------------------

SQL injection happens when user input is directly added to SQL strings:

- ❌ Raw SQL (vulnerable):
  ```python
  user_input = "2024-04-10'); DROP TABLE observations; --"
  query = f"INSERT INTO observations (date, hb) VALUES ('{user_input}', 13.5);"
  cursor.execute(query)
  ```

  💥 This becomes:

  ```sql
  INSERT INTO observations (date, hb) VALUES ('2024-04-10');   
  DROP TABLE observations; -- 
  ```

- ✅ ORM (safe):


  ```python
  obs = Observation(date="2024-04-10'); DROP TABLE observations; --", hb=13.5)
  db.add(obs)
  db.commit()
  ```

  Under the hood, SQLAlchemy sends: `INSERT INTO observations (date, hb) VALUES (%s, %s)`  
  With values passed separately: `["2024-04-10'); DROP TABLE observations; --", 13.5]`

  - ✅ Input is treated as data, not SQL
  - ✅ Injection is blocked by design