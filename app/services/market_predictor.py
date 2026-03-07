def predict_market_direction(sector, sentiment, rsi, momentum):

    score = 0

    # sentiment influence
    if sentiment == "positive":
        score += 2
    elif sentiment == "negative":
        score -= 2

    # sector weight
    if sector == "Banking":
        score += 1
    elif sector == "IT":
        score += 0.5

    # RSI signal
    if rsi is not None:
        if rsi > 60:
            score += 1
        elif rsi < 40:
            score -= 1

    # momentum signal
    if momentum == "UP":
        score += 1
    elif momentum == "DOWN":
        score -= 1

    # final prediction
    if score >= 2:
        direction = "Bullish"
    elif score <= -2:
        direction = "Bearish"
    else:
        direction = "Neutral"

    confidence = min(abs(score) * 20, 90)

    return direction, confidence