EVENT_WEIGHTS = {
    "earnings": 1.3,
    "policy": 1.6,
    "rates": 1.5,
    "war": 1.8,
    "general": 1.0
}

def calculate_impact(sentiment_score, event="general", volatility=1.2):
    weight = EVENT_WEIGHTS.get(event, 1.0)
    return round(sentiment_score * weight * volatility, 2)
def is_high_impact(score):

    if score >= 1.3:
        return True

    if score <= -1.3:
        return True

    return False