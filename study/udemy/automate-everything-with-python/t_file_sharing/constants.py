from os import environ
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

TEMP_FOLDER_NAME = "temp"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

FILE_SAMPLES_URI = "https://filesamples.com/formats/mp3"
MP3_URI_PREFIX = "https://filesamples.com/samples/audio/mp3/"

FILE_UPLOAD_URI = "https://cgi-lib.berkeley.edu/ex/fup.html"
FILE_UPLOAD_POST_URI = "https://cgi-lib.berkeley.edu/ex/fup.cgi"

FILE_STACK_API_KEY = environ.get("FILE_STACK_API_KEY")
