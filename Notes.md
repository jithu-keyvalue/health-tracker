📝 Notes
--------
- Foreign Key: A column that links one table to another — like a reference. It lets you associate related data.
  - user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))

     - user_id is the foreign key.
     - users.id is the target of the foreign key.
     - this means user_id must match an id from the users table.

    This tells DB: every observation belongs to a user from the users table.

- APIRouter: a way to organize and modularize your FastAPI app by grouping related endpoints together into separate routers.

# Relationships
## Step 1: Just use Foreign Key

```
class Message(Base):
    user_id = Column(Integer, ForeignKey("users.id"))
```
  - ✅ You can filter messages by user manually: `db.query(Message).filter(Message.user_id == 1).all()`
  - ✅ Or create linked data like: `new_msg = Message(content="Hello Coach!", user_id=user.id)`
  - ❌ You can’t access msg.user or user.messages.

## Step 2: Add relationship on Message side
```
class Message(Base):
    ...
    user = relationship("User")
```
  - ✅ Now:
    - `msg = db.query(Message).first()`
    - `print(msg.user.name)  # ✅ Works!`
  - ❌ But user.messages still won’t work.

## Step 3: Add relationship to User side
```
class User(Base):
    ...
    messages = relationship("Message")
```
  - ✅ Now:
    - `user = db.query(User).first()`
    - `print(user.messages)  # ✅ list of messages`
  - ✅ Also possible to create linked data in a more object-style way:
    - `new_msg = Message(content="Hello Coach!")`
    - `user.messages.append(new_msg)`
    - `db.add(user)`
    - `db.commit()`
  - ❌ But syncing like this will not work:
    - `user.messages.append(new_msg)`
    - `print(new_msg.user)  # ❌ would be None`

## Step 4: Add back_populates on one side (Message)
```
class Message(Base):
    ...
    user = relationship("User", back_populates="messages")
```
  - ✅ Now:
    - When you do: `msg.user = some_user`, it will auto-add msg to `some_user.messages`.
    - `msg.user_id` is still set automatically.
  - ❌ If you do: `user.messages.append(msg)`, it won’t update `msg.user`.
    - i.e., `msg.user` will still be `None`
    - `msg.user_id` won’t be set either

## Step 5: Add back_populates on both sides
```
class User(Base):
    ...
    messages = relationship("Message", back_populates="user")

class Message(Base):
    ...
    user = relationship("User", back_populates="messages")
```
  - ✅  Full two-way sync! Assign either side, the other reflects it.
```
# Option 1
msg = Message(content="Hello")
msg.user = user
print(user.messages)  # ✅ msg is inside

# Option 2
user.messages.append(msg)
print(msg.user)       # ✅ shows user
print(msg.user_id)    # ✅ is set

```

## Lazy loading in SQLAlchemy
```
user = db.query(User).first()  # Fetches user only
print(user.messages)  # Triggers separate SQL to fetch messages
```
- the related messages are fetched only if required. This is the 'laziness' part.
- Saves memory if you don’t always need related data

## N+1 problem
```
users = db.query(User).all()
for user in users:
    print(user.messages)  # ❌ N extra queries here! Not good!
```
- messages for each user are fetched in separate queries, not efficient
- solution is eager-loading using `joinedload`
```
from sqlalchemy.orm import joinedload
users = db.query(User).options(joinedload(User.messages)).all()
```
- This fetches all users and their messages in a single joined query.
