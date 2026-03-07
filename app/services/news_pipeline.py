import hashlib

from app.services.news_fetcher import fetch_global_news
from app.services.sentiment import analyze_sentiment
from app.services.sector_detector import detect_sector
from app.services.stock_detector import detect_stocks
from app.services.market_brain import market_brain
from app.services.market_predictor import predict_market_direction

from app.database import SessionLocal
from app.models.news import News


IMPORTANT_KEYWORDS = [
    "stock", "market", "share", "equity",
    "nifty", "sensex", "dow", "nasdaq",
    "bank", "interest rate", "inflation",
    "earnings", "profit", "loss",
    "fed", "rbi", "central bank",
    "ipo", "dividend", "results"
]


def is_relevant(text):

    text = text.lower()

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text:
            return True

    return False


def run_news_pipeline():

    db = SessionLocal()

    articles = fetch_global_news()

    for article in articles:

        content = article.get("content") or article.get("title")

        if not content:
            continue

        if not is_relevant(content):
            continue

        title = article.get("title", "")

        news_hash = hashlib.md5(title.encode()).hexdigest()

        exists = db.query(News).filter(News.hash == news_hash).first()

        if exists:
            continue

        # sentiment analysis
        sentiment, score = analyze_sentiment(content)

        # sector detection
        sector = detect_sector(content)

        # stock detection
        stocks = detect_stocks(content)

        # market indicators
        brain = market_brain(sentiment)

        # AI market prediction
        direction, confidence = predict_market_direction(
            sector,
            sentiment,
            brain["nifty"]["rsi"],
            brain["nifty"]["momentum"]
        )

        print("📊 Market Prediction:", direction)
        print("Confidence:", confidence)

        # save to database
        news = News(
            title=title,
            content=content,
            source=article["source"]["name"],
            sentiment=sentiment,
            sector=sector,
            hash=news_hash
        )

        db.add(news)

    db.commit()
    db.close()