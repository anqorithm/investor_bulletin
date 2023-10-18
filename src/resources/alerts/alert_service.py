from resources.alerts.alert_dal import get_all_alerts as get_all_alerts_dal


def get_all_alerts_service(db):
    """Fetches all alert rules from the database."""
    return get_all_alerts_dal(db)
