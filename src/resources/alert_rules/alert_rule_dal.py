from db.models.models import AlertRule
from datetime import datetime


def create_alert_rule(db, rule):
    """Adds and commits a new alert rule to the database."""
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


def get_all_alert_rules(db):
    """Fetches all alert rules from the database."""
    return db.query(AlertRule).all()


def get_alert_rule_by_id(db, id):
    """Fetches a specific alert rule from the database using its ID."""
    return db.query(AlertRule).filter(AlertRule.id == id).first()


def update_alert_rule(db, db_rule, updated_data):
    """Updates a specific alert rule in the database with the provided data."""
    for key, value in updated_data.items():
        setattr(db_rule, key, value)
    db.commit()
    db.refresh(db_rule)
    return db_rule


def delete_alert_rule(db, db_rule):
    """Soft deletes an alert rule by setting its 'deleted_at' timestamp."""
    db_rule.deleted_at = datetime.utcnow()
    db.commit()
