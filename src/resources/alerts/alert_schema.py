from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlertCreate(BaseModel):
    """Create a new alert schema checks"""
    alert_rule_id: int


class AlertUpdate(BaseModel):
    """Upate an existing alert schema checks"""
    alert_rule_id: Optional[int]
