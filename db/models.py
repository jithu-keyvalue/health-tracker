from sqlalchemy import Column, Integer, Date, Float, CheckConstraint
from db.session import Base

class Observation(Base):
    __tablename__ = "observations"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    hb = Column(Float, nullable=False)

    __table_args__ = (
        CheckConstraint("hb > 0", name="check_hb_positive"),
    )
