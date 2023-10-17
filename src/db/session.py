import os
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models.model_base import Base
from utils import utils

utils.load_environment_variables()
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
