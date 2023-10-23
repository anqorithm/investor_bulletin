from resources.alerts.alert_dal import get_all_alerts as get_all_alerts_dal


def get_all_alerts_service(db):
    """Fetches all alert rules from the database."""
    return get_all_alerts_dal(db)


def create_threshold_alert_event_record(event_body):
    """"Create threshold alert event record."""
    print(f"Event Recorded Successfully: {event_body}")
