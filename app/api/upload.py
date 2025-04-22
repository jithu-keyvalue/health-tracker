from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.core.dependencies import get_db, get_current_user
from app.services import upload as upload_service
from app.core.logging_config import logger

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    logger.info(f"Upload attempt by user {current_user.id}")
    return await upload_service.handle_upload(file, db, current_user)
