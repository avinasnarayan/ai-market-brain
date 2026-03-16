from fastapi import APIRouter
from fastapi import Request

router = APIRouter()

option_chain_cache = {}

@router.post("/update-option-chain")

async def update_option_chain(request: Request):

    global option_chain_cache

    data = await request.json()

    option_chain_cache = data

    return {"status": "updated"}

@router.get("/smart-money")

def get_smart_money():

    global option_chain_cache

    if not option_chain_cache:
        return {"error": "No option chain data yet"}

    return option_chain_cache