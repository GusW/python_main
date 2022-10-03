from os import environ
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

FACEBOOK_STANDARD_ID = environ.get("FACEBOOK_STANDARD_ID")
FACEBOOK_TOKEN = environ.get("FACEBOOK_TOKEN")
NEWS_API_KEY = environ.get("NEWS_API_KEY")
OPEN_WEATHER_API_KEY = environ.get("OPEN_WEATHER_API_KEY")

PARENT_FOLDER = Path(__file__).parent.resolve()

TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)

WEATHER_FILE_NAME = "WEATHER.txt"

LANGUAGE_TOOL_API_URI = "https://api.languagetool.org/v2/"
LANGUAGE_TOOL_CHECK_ENDPOINT = f"{LANGUAGE_TOOL_API_URI}check"
