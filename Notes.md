📝 Notes  
--------

- 📦 Alembic  
  A database migration tool for SQLAlchemy. Helps manage schema changes in a structured way.  
  Creates migration scripts to keep track of DB schema changes over time.

- 🛠️ Setting Up Alembic  

  - Configure DB URL:  
    In alembic.ini, set the sqlalchemy.url to point to your Postgres DB.
    ```python
    sqlalchemy.url = postgresql://healthuser:supersecret@localhost:5434/healthdb
    ```

  - Link Models to Alembic:  
    In alembic/env.py, import Base from db.session and your models, then set target_metadata to Base.metadata.
    ```python
    target_metadata = Base.metadata
    ```

- 🔄 Autogenerate Migrations  
  Alembic compares your models to the current DB schema and generates migration scripts.

  ```bash
  alembic revision --autogenerate -m "Create observations table"
  ```

  This will create a migration file in alembic/versions/.

- ⚡ Apply Migrations  
  Run migrations to update the DB schema.

  ```bash
  alembic upgrade head
  ```

  - head applies the most recent migration.

- 🔄 Migrations vs create_all()  

  - create_all(): Creates tables directly but doesn't track changes.
  - Migrations: Track schema changes over time, allow for rollback, and are more flexible in production environments.

- 🎬 Rollback Migrations (Optional)  
  If you want to undo a migration:

  ```bash
  alembic downgrade -1 
  ```

- 🧳 Migration Scripts  
    - Alembic auto-generates scripts for DB schema changes.
    - You can manually edit migration scripts for complex changes (like renaming columns).