from pathlib import Path

TEMP_FOLDER_NAME = "temp"
IMAGES_FOLDER_NAME = "images"
EXERCISE_FOLDER_NAME = "ex01"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

IMAGES_FOLDER_PATH = Path.joinpath(TEMP_FOLDER_PATH, IMAGES_FOLDER_NAME)

EXERCISE_01_PATH = Path.joinpath(TEMP_FOLDER_PATH, EXERCISE_FOLDER_NAME)

VIDEO_MP4_PATH = Path.joinpath(TEMP_FOLDER_PATH, "video.mp4")