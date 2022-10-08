import praw

from y_reddit_posts.constants import (
    REDDIT_CLIENT_ID,
    REDDIT_PASSWORD,
    REDDIT_SECRET,
    REDDIT_USERNAME,
)

reddit_client = praw.Reddit(
    user_agent=True,
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
)
