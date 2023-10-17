from db.models import Alert


def get_all_alerts(db):
    return db.query(Alert).all()
