from fastapi import APIRouter, HTTPException
from resources.market.market_service import get_market_data_serivce

router = APIRouter()


@router.get('/')
def get_market_data_route():
    """Fetch all alerts"""
    try:
        return get_market_data_serivce()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
