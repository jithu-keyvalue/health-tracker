from fastapi import FastAPI, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.session import SessionLocal, Base, engine
from db.models import Observation
from typing import List
import logging
from schemas.observation import ObservationIn, ObservationOut

# Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


# App init
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8001"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/observations")
def add_observation(obs: ObservationIn, db: Session = Depends(get_db)):
    logger.info(f"Inserting via ORM: {obs}")
    db_obs = Observation(date=obs.date, hb=obs.hb)
    db.add(db_obs)
    db.commit()
    return {"message": "Saved"}

@app.get("/observations", response_model=List[ObservationOut])
def get_observations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    logger.info(f"Querying via ORM: skip={skip}, limit={limit}")
    results = db.query(Observation).order_by(Observation.date).offset(skip).limit(limit).all()
    return results
