import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = "redpillcorp@gmail.com"
SENDER_PW = os.getenv("GMAIL_PASSWORD")

PARENT_FOLDER = Path(__file__).parent
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)

ATTACHMENT_PATH = Path.joinpath(TEMP_FOLDER_PATH, "archive.zip")
CONTACTS_PATH = Path.joinpath(TEMP_FOLDER_PATH, "contacts.csv")
