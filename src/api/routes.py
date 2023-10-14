from api.controllers.market_controllers import router as MarketRouter
from api.controllers.rules_controller import router as RuleController


def init_routes(app):
    app.include_router(MarketRouter, prefix="/market-prices", tags=["Market"])
    app.include_router(RuleController, prefix="/alert-rules", tags=["Rules"])
    return app
