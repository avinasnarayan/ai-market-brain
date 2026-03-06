from app.services.market_data import get_index_data
from app.services.market_indicators import analyze_market


def market_brain(news_bias):

    nifty_df, banknifty_df = get_index_data()

    nifty = analyze_market(nifty_df)
    bank = analyze_market(banknifty_df)

    result = {}

    if news_bias == "Bearish" and bank["momentum"] == "DOWN" and bank["rsi"] < 45:

        result["trade"] = "Buy BANKNIFTY PE"
        result["confidence"] = "HIGH"

    elif news_bias == "Bullish" and bank["momentum"] == "UP" and bank["rsi"] > 55:

        result["trade"] = "Buy BANKNIFTY CE"
        result["confidence"] = "HIGH"

    else:

        result["trade"] = "No Trade"
        result["confidence"] = "LOW"

    result["banknifty"] = bank
    result["nifty"] = nifty

    return result