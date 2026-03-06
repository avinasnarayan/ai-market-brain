import requests
from app.config import NEWS_API_KEY

QUERY = "stock market OR economy OR inflation OR interest rates OR RBI OR Fed"

def fetch_global_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": QUERY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 20,
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json().get("articles", [])