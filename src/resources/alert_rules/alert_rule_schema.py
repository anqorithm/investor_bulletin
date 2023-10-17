from pydantic import BaseModel


class AlertRuleCreate(BaseModel):
    name: str
    threshold_price: float
    symbol: str
