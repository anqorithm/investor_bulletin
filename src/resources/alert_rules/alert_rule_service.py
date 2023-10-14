from db.models.models import AlertRule
from resources.alert_rules.alert_rule_dal import (
    create_alert_rule,
    get_all_alert_rules,
    get_alert_rule_by_id,
    update_alert_rule,
    delete_alert_rule
)


def get_all_alert_rules_service(db):
    return get_all_alert_rules(db)


def create_alert_rule_service(rule_data, db):
    rule = AlertRule(**rule_data.dict())
    return create_alert_rule(db, rule)


def get_alert_rule_by_id_service(id, db):
    return get_alert_rule_by_id(db, id)


def update_alert_rule_service(id, rule_data, db):
    db_rule = get_alert_rule_by_id(db, id)
    if not db_rule:
        return None
    return update_alert_rule(db, db_rule, rule_data.dict())


def delete_alert_rule_service(id, db):
    db_rule = get_alert_rule_by_id(db, id)
    if not db_rule:
        return None
    delete_alert_rule(db, db_rule)
    return db_rule
