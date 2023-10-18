from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from db.session import get_session
from resources.alert_rules.alert_rule_schema import (
    AlertRuleCreate,
    AlertRuleUpdate
)
from resources.alert_rules.alert_rule_service import (
    create_alert_rule_service,
    get_all_alert_rules_service,
    get_alert_rule_by_id_service,
    update_alert_rule_service,
    delete_alert_rule_service
)

router = APIRouter()


@router.get("/")
def get_all_alert_rules_route(db: Session = Depends(get_session)):
    """Fetch all alert rules"""
    try:
        return get_all_alert_rules_service(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_alert_rule_route(rule: AlertRuleCreate, db: Session = Depends(get_session)):
    """Create a new alert rule"""
    try:
        return create_alert_rule_service(rule, db)
    except Exception:
        raise HTTPException(
            status_code=500, detail="Failed to create a new rule")


@router.get("/{id}")
def get_alert_rule_by_id_route(id: int, db: Session = Depends(get_session)):
    """Fetch a specific alert rule by its ID"""
    rule = get_alert_rule_by_id_service(id, db)
    if not rule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found")
    return rule


@router.patch("/{id}")
def update_alert_rule_route(id: int, rule: AlertRuleUpdate, db: Session = Depends(get_session)):
    """Update an existing alert rule by its ID"""
    updated_rule = update_alert_rule_service(id, rule, db)
    if not updated_rule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found for update")
    return updated_rule


@router.delete("/{id}")
def delete_alert_rule_route(id: int, db: Session = Depends(get_session)):
    """Delete a specific alert rule by its ID"""
    deleted_rule = delete_alert_rule_service(id, db)
    if not deleted_rule:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rule not found for deletion")
    return {"detail": "Rule deleted successfully"}
