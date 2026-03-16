from fastapi import APIRouter
from app.services.ai_prediction import predict_market

router = APIRouter()

@router.get("/prediction")
def market_prediction():

    result = predict_market()

    return result