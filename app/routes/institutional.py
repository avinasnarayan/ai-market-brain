from fastapi import APIRouter
from app.services.institutional_flow import get_institutional_flow

router = APIRouter()


@router.get("/institutional-flow")

def institutional_flow():

    return get_institutional_flow()