from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.utils.hash import hash_file
from app.utils.pdf import extract_text_from_pdf
from app.tasks.process_file import process_uploaded_file
from app.repositories import upload as upload_repository
from app.db.models import User

async def handle_upload(file: UploadFile, db: Session, user: User):
    content = await file.read()
    file_hash = hash_file(content)

    if upload_repository.exists_by_hash(db, file_hash, user.id):
        raise HTTPException(status_code=400, detail="File already uploaded")

    text_to_process = extract_text_from_pdf(content)[:4000]
    process_uploaded_file.delay(file_hash, text_to_process, str(user.id))

    return {"message": "File accepted. Processing will run in background."}
