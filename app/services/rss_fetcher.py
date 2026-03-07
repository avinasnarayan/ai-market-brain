import feedparser


RSS_SOURCES = [
    "https://feeds.bloomberg.com/markets/news.rss",
    "https://finance.yahoo.com/news/rssindex"
]


def fetch_rss_news():

    articles = []

    for url in RSS_SOURCES:

        feed = feedparser.parse(url)

        for entry in feed.entries:

            title = entry.get("title", "")

            # Some feeds don't provide summary
            content = entry.get("summary", title)

            article = {
                "title": title,
                "content": content,
                "source": {"name": url},
            }

            articles.append(article)

    return articles