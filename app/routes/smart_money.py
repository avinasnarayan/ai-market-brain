from fastapi import APIRouter
from app.services.smart_money import analyze_option_chain

router = APIRouter()

@router.get("/smart-money")

def smart_money():

    return analyze_option_chain()