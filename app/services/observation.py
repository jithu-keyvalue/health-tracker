from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.observation import ObservationIn, ObservationOut
from app.repositories import observation as observation_repo
from app.db.models import User
from typing import List

async def add_observation(
    db: AsyncSession,
    user: User,
    obs: ObservationIn
) -> ObservationOut:
    # Add any business logic/validation here
    db_obs = await observation_repo.create(db, user.id, obs)
    return ObservationOut.model_validate(db_obs)

async def get_user_observations(
    db: AsyncSession,
    user: User
) -> List[ObservationOut]:
    observations = await observation_repo.get_by_user(db, user.id)
    return [ObservationOut.model_validate(obs) for obs in observations]