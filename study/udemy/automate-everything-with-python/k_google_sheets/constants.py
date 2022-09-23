from pathlib import Path

GSHEET_TO_CSV = "gviz/tq?tqx=out:csv&sheet="

PUBLIC_GSHEET_2013_URI = (
    "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84"
    + f"/{GSHEET_TO_CSV}2013"
)
PUBLIC_GSHEET_2014_URI = (
    "https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84"
    + f"/{GSHEET_TO_CSV}2014"
)

PRIVATE_GSHEET_NAME = "weather_private_copy"

ROOT_FOLDER_PATH = Path(__file__).parent.parent.resolve()
GOOGLE_SECRETS_PATH = Path.joinpath(ROOT_FOLDER_PATH, "google-secret.json")
