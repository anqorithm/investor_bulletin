from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AlertCreate(BaseModel):
    alert_rule_id: int


class AlertUpdate(BaseModel):
    alert_rule_id: Optional[int]
