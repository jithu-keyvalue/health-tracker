from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from fastapi import Request, Depends, HTTPException
from app.db.models import User
from app.utils.auth import decode_token

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    # Extract Authorization header
    auth = request.headers.get("Authorization")
    if not auth or not auth.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")

    token = auth.split(" ")[1]
    
    try:
        payload = decode_token(token)
        user_id = payload.get("sub") 
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user