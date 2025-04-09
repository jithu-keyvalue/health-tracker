import os
import csv
import psycopg2
import logging
from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel, Field
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from dotenv import load_dotenv

load_dotenv()

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

logger = logging.getLogger(__name__)


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE = "observations.csv"

# --- Models ---

class Observation(BaseModel):
    date: date
    hb: float = Field(..., example=13.5, gt=0)

# --- Routes ---

@app.post("/observations")
def add_observation(obs: Observation):
    logger.info(f"New observation received: {obs}")

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["date", "hb"])
        writer.writerow([obs.date, obs.hb])

    return {"message": "Saved", "date": obs.date, "hb": obs.hb}

@app.get("/observations", response_model=List[Observation])
def get_observations(skip: int = 0, limit: int = 10):
    logger.info(f"Fetching observations: skip={skip}, limit={limit}")

    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, "r") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    # Sort entries
    data.sort(key=lambda r: r["date"])

    # Slice to get the required page
    paged = data[skip : skip + limit]

    observations = []
    for row in paged:
        obs = Observation(
            date=row["date"],
            hb=float(row["hb"])  # CSV reads everything as strings
        )
        observations.append(obs)

    logger.info(f"Returned {len(observations)} observations.")

    return observations


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5432),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.get("/db-time")
def get_db_time():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW()")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"db_time": 'time'}