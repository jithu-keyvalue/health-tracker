from pydantic import BaseModel, Field
from datetime import date as DateType

class ObservationIn(BaseModel):
    date: DateType
    hb: float = Field(..., gt=0)

class ObservationOut(BaseModel):
    date: DateType
    hb: float
