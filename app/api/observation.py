from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.core.dependencies import get_db, get_current_user
from app.schemas.observation import ObservationIn, ObservationOut
from app.db.models import User
from app.services import observation as observation_service
from app.core.logging_config import logger

router = APIRouter()

@router.post("/", response_model=ObservationOut)
async def add_observation(
    obs: ObservationIn,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> ObservationOut:
    logger.info(f"Adding {obs.metric} observation for user {current_user.id}")
    return await observation_service.add_observation(db, current_user, obs)

@router.get("/", response_model=List[ObservationOut])
async def get_observations(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> List[ObservationOut]:
    logger.info(f"Fetching observations for user {current_user.id}")
    return await observation_service.get_user_observations(db, current_user)