from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing  import List
from app.dependencies import get_db, get_current_user
from app.schemas.observation import ObservationIn, ObservationOut
from app.db.models import Observation, User
from app.logging_config import logger

router = APIRouter()

@router.post("/", response_model=ObservationOut)
def add_observation(obs: ObservationIn, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_obs = Observation(date=obs.date, hb=obs.hb, user_id=current_user.id)
    db.add(db_obs)
    db.commit()
    db.refresh(db_obs)
    logger.info(f"Observation entry successful for user: {current_user.id}")    
    return db_obs

@router.get("/", response_model=List[ObservationOut])
def get_observations(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    observations = db.query(Observation).order_by(Observation.date).filter(Observation.user_id == "current_user.id").all()
    return observations
