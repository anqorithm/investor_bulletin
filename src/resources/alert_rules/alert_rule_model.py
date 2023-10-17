from db.models.model_base import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, func
from sqlalchemy.orm import relationship


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    threshold_price = Column(Float)
    symbol = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    alerts = relationship("Alert", back_populates="alert_rule")
