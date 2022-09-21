from pathlib import Path

PARENT_FOLDER = Path(__file__).parent.resolve()

TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)

STOCK_PERCENTAGE_FILE_NAME = "CBX_PERCENTAGE.txt"

ZSE_URI = "https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6"
