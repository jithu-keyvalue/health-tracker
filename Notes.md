📝 Notes
--------

- 🔗 Foreign Keys
    Link tables together
    ```python
    parent_id = Column(Integer, ForeignKey("parent.id"))
    # Each child belongs to one parent
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/core/constraints.html#sqlalchemy.schema.ForeignKey)

- 🛣️ APIRouter
    Group routes by feature
    ```python
    router = APIRouter()
    app.include_router(router, prefix="/items")
    ```
    [Docs](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

- 🤝 Relationships
    Access related data easily
    ```python
    # 1. Basic Foreign Key only
    class Child(Base):
        parent_id = Column(Integer, ForeignKey("parent.id"))
    # ✅ Manual filtering: db.query(Child).filter(Child.parent_id == parent.id)
    # ❌ Can't do: child.parent

    # 2. Add relationship to Child
    class Child(Base):
        parent = relationship("Parent")
    print(child.parent.name)  # ✅ Works!
    print(parent.children)    # ❌ Doesn't exist

    # 3. Add relationship to Parent
    class Parent(Base):
        children = relationship("Child")
    print(parent.children)     # ✅ Works!
    parent.children.append(c)  # ✅ Works!
    print(c.parent)           # ❌ Not synced back

    # 4. Add back_populates to Child
    class Child(Base):
        parent = relationship("Parent", back_populates="children")
    c.parent = parent           # ✅ Updates parent.children too
    parent.children.append(c)   # ❌ Doesn't update c.parent

    # 5. Add back_populates to both
    class Child(Base):
        parent = relationship("Parent", back_populates="children")
    class Parent(Base):
        children = relationship("Child", back_populates="parent")
    
    # Everything works:
    c.parent = parent             # ✅ Both sides sync
    parent.children.append(c)     # ✅ Both sides sync
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/relationships.html)

- 🔄 Lazy Loading
    Load related data on demand
    ```python
    # Loads parent first
    parent = db.query(Parent).first()
    
    # Loads children only when needed
    print(parent.children)  # Separate query
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html#lazy-loading)

- ⚡ N+1 Problem
    Avoid multiple queries
    ```python
    # ❌ N+1 queries
    for parent in parents:
        print(parent.children)

    # ✅ Single query with join
    from sqlalchemy.orm import joinedload
    parents = db.query(Parent).options(
        joinedload(Parent.children)
    ).all()
    ```
    [Docs](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html#joined-eager-loading)
