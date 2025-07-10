from uuid import UUID
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import Observation
from app.schemas.observation import ObservationIn

async def create(db: AsyncSession, user_id: UUID, obs: ObservationIn) -> Observation:
    db_obs = Observation(
        user_id=user_id,
        date=obs.date,
        metric=obs.metric,
        value=obs.value
    )
    db.add(db_obs)
    await db.commit()
    await db.refresh(db_obs)
    return db_obs

async def get_by_user(db: AsyncSession, user_id: UUID) -> list[Observation]:
    stmt = select(Observation).where(Observation.user_id == user_id)
    result = await db.execute(stmt)
    return list(result.scalars().all())