from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(ROOT_FOLDER, TEMP_FOLDER_NAME)

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"

YAHOO_FINANCE_URI = "https://query1.finance.yahoo.com/v7/finance/download/"
YAHOO_FINANCE_URI_SUFFIX = "&events=history&includeAdjustedClose=true"

X_RATES_CALCULATOR_URI = "https://www.x-rates.com/calculator/"
