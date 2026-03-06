from transformers import pipeline

sentiment_model = None


def get_model():
    global sentiment_model

    if sentiment_model is None:
        sentiment_model = pipeline(
            "sentiment-analysis",
            model="ProsusAI/finbert"
        )

    return sentiment_model


def analyze_sentiment(text):

    model = get_model()

    result = model(text[:512])[0]

    label = result["label"]
    score = result["score"]

    return label.lower(), score