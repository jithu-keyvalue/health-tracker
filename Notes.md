📝 Notes
--------

- 🔄 Database Migrations
    Track schema changes over time
    ```python
    # Instead of this
    Base.metadata.create_all()

    # Use migrations
    alembic upgrade head
    ```
    [Docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

- 📝 Migration Files
    Auto-generate from models
    ```bash
    # Create migration
    alembic revision --autogenerate -m "add users"

    # Apply latest
    alembic upgrade head

    # Rollback one step
    alembic downgrade -1
    ```
    [Docs](https://alembic.sqlalchemy.org/en/latest/autogenerate.html)

- ⚙️ Configuration
    Set up database connection
    ```python
    # alembic.ini
    sqlalchemy.url = postgresql://user:pass@localhost/db

    # env.py
    from myapp.models import Base
    target_metadata = Base.metadata
    ```
    [Docs](https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file)

- 🔍 Review Migrations
    Always check generated files
    ```python
    # migrations/versions/abc123_add_users.py
    def upgrade():
        op.create_table(
            'users',
            sa.Column('id', sa.Integer())
        )
    ```
    [Docs](https://alembic.sqlalchemy.org/en/latest/ops.html)