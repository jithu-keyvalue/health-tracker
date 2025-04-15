import hashlib
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_current_user
from app.db.models import UploadedFile
from app.db.models import User
from app.utils.hash import hash_file
from app.utils.pdf import extract_text_from_pdf
from app.tasks.process_file import process_uploaded_file
from app.logging_config import logger

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    content = await file.read()
    file_hash = hash_file(content)

    # Check for duplicate
    exists = db.query(UploadedFile).filter_by(hash=file_hash, user_id=current_user.id).first()
    if exists:
        raise HTTPException(status_code=400, detail="File already uploaded")

    logger.info(f"Received new file upload from user {current_user.id}")

    # Send to Celery for async processing
    text_to_process = extract_text_from_pdf(content)[:4000]

    process_uploaded_file.delay(file_hash, text_to_process, str(current_user.id))

    return {"message": "File accepted. Processing will run in background."}
