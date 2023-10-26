""" Market Threshold Checker """
"""_summary_
This script uses a Celery task to check market prices and triggers alerts if predefined thresholds are reached.
"""




from worker.app import celery_app
from resources.market.market_service import get_market_data_service
from resources.alert_rules.alert_rule_service import get_all_alert_rules_service
from core.messaging import publish_threshold_alert
from db.session import get_session
@celery_app.task
def check_thresholds():
    try:
        market_data = get_market_data()
        db = next(get_session())
        alert_rules = get_all_alert_rules_service(db)
        for rule in alert_rules:
            symbol = rule.symbol
            threshold_price = rule.threshold_price
            current_price = float(market_data[symbol]['price'])
            if threshold_price < current_price:
                print("###############################################################")
                print(f"current price {current_price}")
                print(f"threshold price {threshold_price}")
                publish_threshold_alert('THRESHOLD_ALERT', {
                    'symbol': symbol,
                    'current_price': current_price,
                    'threshold': threshold_price
                })
    except Exception as e:
        print(f"An error occurred: {e}")


def get_market_data():
    try:
        market_data = get_market_data_service()
    except Exception as e:
        print(f"Error fetching market data: {e}")
        market_data = {
            "AAPL": {"price": "173.39000"},
            "MSFT": {"price": "330.79001"},
            "GOOG": {"price": "140.21001"},
            "AMZN": {"price": "128.57899"},
            "META": {"price": "312.56009"}
        }
    return market_data
