import uuid
from db.session import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Date, Float, CheckConstraint

class Observation(Base):
    __tablename__ = "observations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    date = Column(Date, nullable=False)
    hb = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint("hb > 0", name="check_hb_positive"),
    )


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)