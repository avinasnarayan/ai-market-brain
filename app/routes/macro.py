from fastapi import APIRouter
from app.services.macro_brain import macro_prediction

router = APIRouter()

@router.get("/premarket")

def premarket_outlook():

    return macro_prediction()