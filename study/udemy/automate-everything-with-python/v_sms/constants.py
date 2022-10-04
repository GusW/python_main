from os import environ
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = environ.get("TWILIO_PHONE_NUMBER")
TWILIO_PHONE_NUMBER_DESTINATION = environ.get("TWILIO_PHONE_NUMBER_DESTINATION")
