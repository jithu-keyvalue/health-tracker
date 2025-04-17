from sqlalchemy.orm import Session
from app.db.models import User
from app.schemas.user import UserCreate

def get_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: UserCreate):
    from app.utils.auth import hash_password
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        password_hash=hash_password(user_data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "user": {"name": new_user.name, "email": new_user.email}}
