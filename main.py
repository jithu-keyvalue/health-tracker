import os
import logging
import psycopg2
from dotenv import load_dotenv
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List
from datetime import date as DateType

# Load .env
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

# FastAPI app
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model
class Observation(BaseModel):
    date: DateType = Field(..., example="2024-04-10")
    hb: float = Field(..., example=13.5, gt=0)

# DB connection
def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", 5434),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.post("/observations")
def add_observation(obs: Observation):
    logger.info(f"Saving observation: {obs}")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO observations (date, hb) VALUES (%s, %s)",
        (obs.date, obs.hb)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Saved", "date": obs.date, "hb": obs.hb}

@app.get("/observations", response_model=List[Observation])
def get_observations(skip: int = 0, limit: int = 10):
    logger.info(f"Fetching observations: skip={skip}, limit={limit}")
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT date, hb FROM observation ORDER BY date OFFSET %s LIMIT %s",
        (skip, limit)
    )
    rows = cur.fetchall()
    cur.close()
    conn.close()
    observations = [{"date": r[0], "hb": r[1]} for r in rows]
    logger.info(f"Returned {len(observations)} rows")
    return observations
