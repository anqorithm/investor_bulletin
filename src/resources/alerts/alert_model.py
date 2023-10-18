from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from db.models.model_base import Base
from sqlalchemy.orm import relationship


class Alert(Base):
    """Alert model"""
    __tablename__ = 'alerts'

    id = Column(Integer, primary_key=True)
    alert_rule_id = Column(Integer, ForeignKey('alert_rules.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    alert_rule = relationship("AlertRule", back_populates="alerts")
