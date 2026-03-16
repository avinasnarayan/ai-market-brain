from fastapi import APIRouter
from app.services.signal_engine import generate_signal

router = APIRouter()

@router.get("/signal")

def get_signal():

    return generate_signal()