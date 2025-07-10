from fastapi import UploadFile, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.utils.hash import hash_file
from app.utils.pdf import extract_text_from_pdf
from app.tasks.process_file import process_uploaded_file
from app.repositories import upload as upload_repo
from app.db.models import User

async def handle_upload(file: UploadFile, db: AsyncSession, user: User) -> dict:
    content = await file.read()
    file_hash = hash_file(content)

    if await upload_repo.exists_by_hash(db, file_hash, user.id):
        raise HTTPException(status_code=400, detail="File already uploaded")

    text_to_process = extract_text_from_pdf(content)[:4000]
    process_uploaded_file.delay(file_hash, text_to_process, str(user.id))

    return {"message": "File accepted. Processing will run in background."}
