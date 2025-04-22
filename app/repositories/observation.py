from sqlalchemy.orm import Session
from typing import List
from app.db.models import Observation
from app.schemas.observation import ObservationIn

def create_observation(db: Session, user_id: str, obs_data: ObservationIn) -> Observation:
    obs = Observation(
        date=obs_data.date,
        metric=obs_data.metric,
        value=obs_data.value,
        file_id=obs_data.file_id,
        user_id=user_id
    )
    db.add(obs)
    db.commit()
    db.refresh(obs)
    return obs

def get_observations_for_user(db: Session, user_id: str) -> List[Observation]:
    return (
        db.query(Observation)
        .filter(Observation.user_id == "user_id")
        .order_by(Observation.date)
        .all()
    )