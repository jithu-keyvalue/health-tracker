from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import UploadedFile

async def exists_by_hash(db: AsyncSession, file_hash: str, user_id: UUID) -> bool:
    stmt = select(UploadedFile).where(
        UploadedFile.hash == file_hash,
        UploadedFile.user_id == user_id
    )
    result = await db.execute(stmt)
    return result.first() is not None

async def create(db: AsyncSession, user_id: UUID, file_hash: str) -> UploadedFile:
    file = UploadedFile(user_id=user_id, hash=file_hash)
    db.add(file)
    await db.commit()
    await db.refresh(file)
    return file
