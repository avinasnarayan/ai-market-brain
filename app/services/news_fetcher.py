from app.services.rss_fetcher import fetch_rss_news
import requests
import os

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def fetch_global_news():

    articles = []

    # RSS sources
    try:
        rss_articles = fetch_rss_news()
        articles.extend(rss_articles)
    except Exception as e:
        print("RSS fetch error:", e)

    # NewsAPI
    try:

        url = "https://newsapi.org/v2/everything"

        params = {
            "q": "stock market OR economy OR inflation OR interest rates OR RBI OR Fed",
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 20,
            "apiKey": NEWS_API_KEY
        }

        response = requests.get(url, params=params)

        if response.status_code != 429:
            data = response.json()
            articles.extend(data.get("articles", []))

        else:
            print("NewsAPI rate limit reached")

    except Exception as e:
        print("NewsAPI error:", e)

    return articles