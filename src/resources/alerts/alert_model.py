""" Alert Model """
from db.models.model_base import Base
from sqlalchemy import Column, Integer


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
