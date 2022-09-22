import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

GMAIL_SENDER_EMAIL = os.getenv("GMAIL_SENDER")
GMAIL_SENDER_PW = os.getenv("GMAIL_PASSWORD")

OUTLOOK_SENDER_EMAIL = os.getenv("OUTLOOK_SENDER")
OUTLOOK_SENDER_PW = os.getenv("OUTLOOK_PASSWORD")
OUTLOOK_SMTP_SERVER = os.getenv("OUTLOOK_SMTP_SERVER")
OUTLOOK_SMTP_PORT = os.getenv("OUTLOOK_SMTP_PORT")

RECEIVER = os.getenv("RECEIVER")

PARENT_FOLDER = Path(__file__).parent
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)

ATTACHMENT_PATH = Path.joinpath(TEMP_FOLDER_PATH, "archive.zip")
CONTACTS_PATH = Path.joinpath(TEMP_FOLDER_PATH, "contacts.csv")
