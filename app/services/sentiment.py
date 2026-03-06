from transformers import pipeline

# Load FinBERT model once
sentiment_model = pipeline(
    "sentiment-analysis",
    model="ProsusAI/finbert"
)

def analyze_sentiment(text: str):
    """
    Analyze sentiment of financial news text.
    Returns: (label, score)
    """
    result = sentiment_model(text[:512])[0]
    label = result["label"].lower()

    if label == "positive":
        return "positive", 1
    elif label == "negative":
        return "negative", -1
    else:
        return "neutral", 0