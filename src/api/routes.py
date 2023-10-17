from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as RuleController
from api.controllers.alerts_controller import router as AlertController


def init_routes(app):
    app.include_router(
        MarketRouter, prefix="/api/v1/market-prices", tags=["Market"])
    app.include_router(
        RuleController, prefix="/api/v1/alert-rules", tags=["Rules"])
    app.include_router(
        AlertController, prefix="/api/v1/alerts", tags=["Alerts"])
    return app
