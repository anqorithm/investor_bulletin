""" Alert Rule Model """
from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    threshold_price = Column(Float)
    symbol = Column(String, index=True)
