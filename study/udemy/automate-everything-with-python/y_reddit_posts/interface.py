from datetime import datetime, timedelta
from enum import Enum
from pprint import pprint
from typing import Optional, Union, Type

from praw.reddit import Submission

from y_reddit_posts.client import reddit_client


class RedditPostFields(str, Enum):
    TITLE = "title"
    TEXT = "text"
    COMMENTS = "comments"


POST_UNPACKED = Type[dict[RedditPostFields, Union[str, list[str]]]]


def _unpack_post(post: Submission) -> POST_UNPACKED:
    return {
        RedditPostFields.TITLE: post.title,
        RedditPostFields.TEXT: post.selftext,
        # top-level comments
        RedditPostFields.COMMENTS: [comm.body for comm in post.comments],
    }


def scrape_post(post_url: str) -> POST_UNPACKED:
    post = reddit_client.submission(url=post_url)
    return _unpack_post(post)


def get_new_posts_in_subreddit(
    subreddit_name: str, last_hours: int = 24
) -> Optional[list[POST_UNPACKED]]:
    now = datetime.utcnow()
    subreddit = reddit_client.subreddit(subreddit_name)
    return [
        _unpack_post(post)
        for post in subreddit.new()
        if now - datetime.utcfromtimestamp(post.created) >= timedelta(hours=last_hours)
    ]


def create_post(
    subreddit_name: str = "pythonsandlot",
    title: str = "Hello World",
    content: str = "Hello Again!",
) -> Optional[Submission]:
    try:
        subreddit = reddit_client.subreddit(subreddit_name)
        subreddit.validate_on_submit = True
        return subreddit.submit(title=title, selftext=content)
    except Exception as err:
        print(f"!!!ERROR!!! Could not create post: {err}")


def reply_post(target_post: Submission, reply_message: str) -> None:
    try:
        target_post.reply(reply_message)
    except Exception as err:
        print(f"!!!ERROR!!! Could not reply to post {target_post.id}: {err}")


def main():
    url = "https://www.reddit.com/r/StockMarket/comments/xw753j/twitter_jumped_22_after_elon_musk_revives_deal_to/"
    pprint(scrape_post(url))

    subreddit = "glassblowing"
    pprint(get_new_posts_in_subreddit(subreddit))

    create_post(
        title="PEP 634 – Structural Pattern Matching",
        content="""
The pattern matching process takes as input a pattern (following case) and a subject value (following match).
Phrases to describe the process include “the pattern is matched with (or against) the subject value” and
“we match the pattern against (or with) the subject value”.

The primary outcome of pattern matching is success or failure. In case of success we may say “the pattern succeeds”,
“the match succeeds”, or “the pattern matches the subject value”.
""",
    )


if __name__ == "__main__":
    main()
