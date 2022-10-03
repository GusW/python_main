from pathlib import Path


TEMP_FOLDER_NAME = "temp"
DATABASE_NAME = "database.db"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

DATABASE_PATH = Path.joinpath(TEMP_FOLDER_PATH, DATABASE_NAME)
