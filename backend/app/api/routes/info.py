from fastapi import APIRouter, HTTPException

from service.stock_dao import StockDAO

router = APIRouter(prefix="/info", tags=["info"])

stock_dao = StockDAO()

@router.get("/")
def display_stock_info():
    return {
        "message": "Hello"
    }