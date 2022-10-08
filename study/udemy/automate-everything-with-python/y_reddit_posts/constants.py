from os import environ

from dotenv import load_dotenv

load_dotenv()


REDDIT_CLIENT_ID = environ.get("REDDIT_CLIENT_ID")
REDDIT_PASSWORD = environ.get("REDDIT_PASSWORD")
REDDIT_SECRET = environ.get("REDDIT_SECRET")
REDDIT_USERNAME = environ.get("REDDIT_USERNAME")
