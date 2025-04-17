from sqlalchemy.orm import Session
from app.db.models import User, Observation
from app.schemas.observation import ObservationIn
from app.repositories import observation as observation_repository

def add_observation(db: Session, user: User, obs_data: ObservationIn) -> Observation:
    return observation_repository.create_observation(db, user.id, obs_data)

def list_observations(db: Session, user: User):
    return observation_repository.get_observations_for_user(db, user.id)