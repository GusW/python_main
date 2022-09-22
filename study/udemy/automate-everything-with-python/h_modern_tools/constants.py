from pathlib import Path

PARENT_FOLDER = Path(__file__).parent.resolve()
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)
