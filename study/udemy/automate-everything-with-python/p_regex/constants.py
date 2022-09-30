from pathlib import Path

TEMP_FOLDER_NAME = "temp"
FILES_FOLDER_NAME = "files"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

FILES_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, FILES_FOLDER_NAME)
