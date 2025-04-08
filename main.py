from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel, Field
from typing import List
import csv
import os


app = FastAPI()
CSV_FILE = "observations.csv"

# --- Models ---

class Observation(BaseModel):
    date: date
    hb: float = Field(..., example=13.5, gt=30)

# --- Routes ---

@app.post("/observations")
def add_observation(obs: Observation):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "hb"])
        writer.writerow([obs.date, obs.hb])

    return {"message": "Saved", "date": obs.date, "hb": obs.hb}

@app.get("/observations", response_model=List[Observation])
def get_observations(skip: int = 0, limit: int = 10):
    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Sort entries
    data.sort(key=lambda r: r["hb"])

    # Slice to get the required page
    paged = data[skip : skip + limit]

    observations = []
    for row in paged:
        obs = Observation(
            date=row["date"],
            hb=float(row["hb"])  # CSV reads everything as strings
        )
        observations.append(obs)

    return observations
