from db.models.models import AlertRule


def create_alert_rule(db, rule):
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


def get_all_alert_rules(db):
    return db.query(AlertRule).all()


def get_alert_rule_by_id(db, id):
    return db.query(AlertRule).filter(AlertRule.id == id).first()


def update_alert_rule(db, db_rule, updated_data):
    for key, value in updated_data.items():
        setattr(db_rule, key, value)
    db.commit()
    db.refresh(db_rule)
    return db_rule


def delete_alert_rule(db, db_rule):
    db.delete(db_rule)
    db.commit()
