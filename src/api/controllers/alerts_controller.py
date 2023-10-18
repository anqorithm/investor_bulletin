from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_session
from resources.alerts.alert_service import get_all_alerts_service

router = APIRouter()


@router.get("/")
def get_all_alerts_route(db: Session = Depends(get_session)):
    """Fetch all alerts"""
    try:
        return get_all_alerts_service(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
