from sqlalchemy.orm import Session
from db.session import SessionLocal

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
