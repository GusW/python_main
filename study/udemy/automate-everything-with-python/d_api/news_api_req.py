from datetime import date, timedelta
from typing import Any, Optional
import requests

from d_api.constants import NEWS_API_KEY

DATE_FORMAT = "%Y-%m-%d"

YESTERDAY = date.today() - timedelta(days=1)
A_MONTH_AGO = YESTERDAY - timedelta(days=30)


def _handle_everything_news_uri(
    topic: str,
    from_date: str = A_MONTH_AGO.strftime(DATE_FORMAT),
    to_date: str = YESTERDAY.strftime(DATE_FORMAT),
    language: str = "en",
    sort_by: str = "popularity",
) -> str:
    return (
        f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&"
        + f"to={to_date}&sortBy={sort_by}&language={language}&apiKey={NEWS_API_KEY}"
    )


def _handle_top_headlines_uri(country: str = "us") -> str:
    return (
        f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"
    )


def get_news(news_uri: str) -> Optional[dict[str, Any]]:
    if (req := requests.get(news_uri)) and req.status_code == 200:
        return req.json()


def _unpack_articles(articles: list[str]):
    print("#\tTITLE\tDESCRIPTION")
    for idx, article in enumerate(articles, 1):
        print(f"{idx}\t{article.get('title')}\t{article.get('description')}")


def list_articles_by_topic(
    topic: str,
    from_date: str = A_MONTH_AGO.strftime(DATE_FORMAT),
    to_date: str = YESTERDAY.strftime(DATE_FORMAT),
    language: str = "en",
    sort_by: str = "popularity",
) -> None:
    news_uri = _handle_everything_news_uri(topic, from_date, to_date, language, sort_by)
    if news := get_news(news_uri):
        _unpack_articles(news.get("articles"))


def list_articles_by_country(country: str = "us"):
    news_uri = _handle_top_headlines_uri(country)
    if news := get_news(news_uri):
        _unpack_articles(news.get("articles"))


def main():
    list_articles_by_topic(
        "space", from_date=(YESTERDAY - timedelta(days=2)).strftime(DATE_FORMAT)
    )
    print("\n\n")
    list_articles_by_country()


if __name__ == "__main__":
    main()
