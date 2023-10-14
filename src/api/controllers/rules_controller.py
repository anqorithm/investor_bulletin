from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.session import get_session
from resources.alert_rules.alert_rule_schema import AlertRuleCreate
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
    return get_all_alert_rules_service(db)


@router.post("/")
async def create_alert_rule_route(rule: AlertRuleCreate, db: Session = Depends(get_session)):
    return create_alert_rule_service(rule, db)


@router.get("/{id}")
def get_alert_rule_by_id_route(id: int, db: Session = Depends(get_session)):
    rule = get_alert_rule_by_id_service(id, db)
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return rule


@router.patch("/{id}")
def update_alert_rule_route(id: int, rule: AlertRuleCreate, db: Session = Depends(get_session)):
    updated_rule = update_alert_rule_service(id, rule, db)
    if not updated_rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return updated_rule


@router.delete("/{id}")
def delete_alert_rule_route(id: int, db: Session = Depends(get_session)):
    deleted_rule = delete_alert_rule_service(id, db)
    if not deleted_rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    return {"status": "rule deleted"}
