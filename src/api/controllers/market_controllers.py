from fastapi import APIRouter
from resources.market.market_service import get_market_data_serivce
router = APIRouter()


@router.get('/')
def get_market_data_route():
    """Fetch all alerts"""
    return get_market_data_serivce()
