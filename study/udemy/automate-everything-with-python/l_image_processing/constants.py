from pathlib import Path


PARENT_FOLDER_PATH = Path(__file__).parent.resolve()
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

EX_01_FOLDER_NAME = "ex01"
EX_01_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, EX_01_FOLDER_NAME)
EX_01_IMAGES_PATH = Path.joinpath(EX_01_FOLDER_PATH, "images")
EX_01_GRAYIMAGES_PATH = Path.joinpath(EX_01_FOLDER_PATH, "grayimages")
EX_02_RESIZEDIMAGES_PATH = Path.joinpath(EX_01_FOLDER_PATH, "resizedimages")
