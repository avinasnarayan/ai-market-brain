def predict_market_direction(sentiment, impact):

    if impact >= 1.3:
        return "🟢 Bullish"

    if impact <= -1.3:
        return "🔴 Bearish"

    return "🟡 Neutral"