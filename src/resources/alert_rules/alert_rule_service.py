from db.models.models import AlertRule
from resources.alert_rules.alert_rule_dal import (
    create_alert_rule,
    get_all_alert_rules,
    get_alert_rule_by_id,
    update_alert_rule,
    delete_alert_rule
)


def get_all_alert_rules_service(db):
    """Fetches all alert rules from the database"""
    return get_all_alert_rules(db)


def create_alert_rule_service(rule_data, db):
    """Creates a new alert rule based on provided data"""
    rule = AlertRule(**rule_data.dict())
    return create_alert_rule(db, rule)


def get_alert_rule_by_id_service(id, db):
    """Fetches a specific alert rule by its ID"""
    return get_alert_rule_by_id(db, id)


def update_alert_rule_service(id, rule_data, db):
    """Updates a specific alert rule based on provided ID and data"""
    db_rule = get_alert_rule_by_id(db, id)
    if not db_rule:
        return None
    return update_alert_rule(db, db_rule, rule_data.dict())


def delete_alert_rule_service(id, db):
    """Deletes a specific alert rule by its ID"""
    db_rule = get_alert_rule_by_id(db, id)
    if not db_rule or db_rule.deleted_at:
        return None
    delete_alert_rule(db, db_rule)
    return db_rule
