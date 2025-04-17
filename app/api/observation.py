from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.dependencies import get_db, get_current_user
from app.schemas.observation import ObservationIn, ObservationOut
from app.db.models import User
from app.services import observation as observation_service
from app.logging_config import logger

router = APIRouter()

@router.post("/", response_model=ObservationOut)
def add_observation(
    obs: ObservationIn,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    logger.info(f"Adding {obs.metric} observation for user {current_user.id}")
    return observation_service.add_observation(db, current_user, obs)


@router.get("/", response_model=List[ObservationOut])
def get_observations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return observation_service.list_observations(db, current_user)