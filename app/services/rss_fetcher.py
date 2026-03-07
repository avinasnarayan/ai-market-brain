import feedparser

RSS_SOURCES = [
    "https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best",
    "https://feeds.bloomberg.com/markets/news.rss",
    "https://finance.yahoo.com/news/rssindex"
]


def fetch_rss_news():

    articles = []

    for url in RSS_SOURCES:

        feed = feedparser.parse(url)

        for entry in feed.entries:

            article = {
                "title": entry.title,
                "content": entry.summary,
                "source": {"name": entry.get("source", "RSS")},
            }

            articles.append(article)

    return articles