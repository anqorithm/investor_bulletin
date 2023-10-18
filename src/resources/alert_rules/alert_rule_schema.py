from pydantic import BaseModel
from typing import Optional


class AlertRuleCreate(BaseModel):
    """Create a new alert rule schema checks"""
    name: str
    threshold_price: float
    symbol: str


class AlertRuleUpdate(BaseModel):
    """Upate an existing alert rule schema checks"""
    name: Optional[str] = None
    threshold_price: Optional[float] = None
    symbol: Optional[str] = None
