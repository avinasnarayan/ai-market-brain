def calculate_confidence(sentiment_score, impact_score, stocks):

    confidence = 50

    # sentiment strength
    if sentiment_score > 0:
        confidence += 10
    elif sentiment_score < 0:
        confidence += 10

    # strong impact
    if abs(impact_score) > 1.5:
        confidence += 20
    elif abs(impact_score) > 1.0:
        confidence += 10

    # company mentioned
    if stocks:
        confidence += 10

    if confidence > 100:
        confidence = 100

    return confidence

def confidence_label(confidence):

    if confidence >= 80:
        return "HIGH"

    if confidence >= 60:
        return "MEDIUM"

    return "LOW"