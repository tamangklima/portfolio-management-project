import requests

try:
    import config
except ImportError:
    import Core.config as config

api_key = config.news_key


def latest_news():
    """Request CNBC articles from News API and returns a multidimensional
       array."""

    url = "https://newsapi.org/v2/top-headlines?"
    source = "cnbc"
    params = {"apiKey": api_key,
              "sources": source,
              "pagesize": 20}

    response = requests.get(url, params=params)
    news = response.json()
    news_articles = news["articles"]
    formatted_articles = []

    for article in news_articles:
        source = article["source"]["name"]
        headline = "{}...".format(article["title"][0:46])
        link = article["url"]
        formatted_articles.append([headline,
                                  source,
                                  link])

    return formatted_articles
