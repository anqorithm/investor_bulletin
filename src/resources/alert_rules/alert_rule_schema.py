from pydantic import BaseModel
from typing import Optional


class AlertRuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str


class AlertRuleUpdate(BaseModel):
    name: Optional[str] = None
    threshold_price: Optional[float] = None
    symbol: Optional[str] = None
