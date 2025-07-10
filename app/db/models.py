import uuid
from app.db.session import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Observation(Base):
    __tablename__ = "observations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    date = Column(Date, nullable=False)
    metric = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="observations")

    file_id = Column(String, ForeignKey("uploaded_files.id"), nullable=True)
    file = relationship("UploadedFile", back_populates="observations")

    __table_args__ = (
        CheckConstraint("hb > 0", name="check_hb_positive"),
    )


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    observations = relationship("Observation", back_populates="user")
    files = relationship("UploadedFile", back_populates="user")


class UploadedFile(Base):
    __tablename__ = "uploaded_files"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    hash = Column(String, unique=True, nullable=False)
    uploaded_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="files")
    observations = relationship("Observation", back_populates="file")