import hashlib

from app.services.news_fetcher import fetch_global_news
from app.services.sentiment import analyze_sentiment
from app.services.impact import calculate_impact, is_high_impact
from app.services.sector_detector import detect_sector
from app.services.stock_detector import detect_stocks
from app.services.confidence_engine import calculate_confidence, confidence_label
from app.services.market_brain import market_brain
from app.services.notifier import send_notification

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


def is_relevant(text: str):

    text = text.lower()

    for keyword in IMPORTANT_KEYWORDS:
        if keyword in text:
            return True

    return False


def run_news_pipeline():

    db = SessionLocal()

    articles = fetch_global_news()

    for article in articles:

        content = article.get("content")

        if not content:
            continue

        if not is_relevant(content):
            continue

        title = article.get("title", "")

        news_hash = hashlib.md5(title.encode()).hexdigest()

        exists = db.query(News).filter(News.hash == news_hash).first()

        if exists:
            continue

        # Sentiment
        sentiment, score = analyze_sentiment(content)

        # Impact score
        impact = calculate_impact(score)

        # Sector detection
        sector = detect_sector(content)

        # Stock detection
        stocks = detect_stocks(content)

        # Confidence engine
        confidence = calculate_confidence(score, impact, stocks)
        confidence_level = confidence_label(confidence)

        # News bias
        news_bias = "Bullish" if impact > 0 else "Bearish"

        # AI Market Brain
        brain = market_brain(news_bias)

        # Send alert if high impact
        if is_high_impact(impact):

            send_notification(
                title,
                sentiment,
                impact,
                article["source"]["name"],
                sector,
                stocks,
                confidence,
                confidence_level,
                brain
            )

        news = News(
            title=title,
            content=content,
            source=article["source"]["name"],
            sentiment=sentiment,
            impact_score=impact,
            sector=sector,
            hash=news_hash
        )

        db.add(news)

    db.commit()
    db.close()