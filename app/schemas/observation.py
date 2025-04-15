from pydantic import BaseModel, Field
from datetime import date as DateType
from typing import Optional

class ObservationIn(BaseModel):
    date: DateType
    metric: str = Field(..., example="hb")
    value: float = Field(..., gt=0)
    file_id: Optional[str] = None  # optional field

class ObservationOut(BaseModel):
    date: DateType
    metric: str
    value: float
    file_id: Optional[str]