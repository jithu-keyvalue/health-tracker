📝 Notes
--------

- 🧱 SQLAlchemy Model
    Define tables as classes
    ```python
    class Item(Base):
        __tablename__ = "items"
        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=False)
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/mapping_styles.html)

- 📝 Database Operations
    Work with data as objects
    ```python
    # Create
    item = Item(name="test")
    db.add(item)
    db.commit()  # Save to database

    # Query
    items = db.query(Item).all()
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)

- 🔄 Session Management
    Handle database connections
    ```python
    # Dependency Injection
    def get_db():
        db = SessionLocal()
        try:
            yield db  # Provides session to endpoint
        finally:
            db.close()  # Auto-cleanup

    # Use in endpoint
    def create_item(item: ItemIn, db: Session = Depends(get_db)):
        db_item = Item(**item.dict())
        db.add(db_item)
        db.commit()
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it)

- 🏗️ Create Tables
    Auto-create from models
    ```python
    # Create all tables on startup
    Base.metadata.create_all(bind=engine)
    ```
    Limitations:
    - Can't track schema changes
    - No way to rollback changes
    - Not suitable for production
    [Docs](https://docs.sqlalchemy.org/en/20/core/metadata.html#creating-and-dropping-database-tables)

- 🛡️ SQL Injection Protection
    Raw SQL vs ORM approach
    ```python
    # Raw SQL (vulnerable)
    name = "Robert'); DROP TABLE items; --"
    cur.execute(f"INSERT INTO items (name) VALUES ('{name}')")

    # ORM (safe)
    db.add(Item(name="Robert'); DROP TABLE items; --"))
    db.commit()
    ```
    ORM sends values separately from query:
    ```sql
    INSERT INTO items (name) VALUES ($1)  -- Query
    ["Robert'); DROP TABLE items; --"]     -- Values
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/faq/sqlexpressions.html#how-do-i-render-sql-expressions-as-strings-possibly-with-bound-parameters-inlined)