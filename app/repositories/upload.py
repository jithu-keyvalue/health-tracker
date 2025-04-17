from sqlalchemy.orm import Session
from app.db.models import UploadedFile

def exists_by_hash(db: Session, file_hash: str, user_id: str) -> bool:
    return db.query(UploadedFile).filter_by(hash=file_hash, user_id=user_id).first() is not None
