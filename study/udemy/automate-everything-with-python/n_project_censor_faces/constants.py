from pathlib import Path

TEMP_FOLDER_NAME = "temp"
VIDEO_NAME = "video-sample.mp4"
SMILE_VIDEO_NAME = "smile.mp4"
CAT_FILE_NAME = "cat.jpg"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

VIDEO_PATH = Path.joinpath(TEMP_FOLDER_PATH, VIDEO_NAME)
SMILE_VIDEO_PATH = Path.joinpath(TEMP_FOLDER_PATH, SMILE_VIDEO_NAME)


CAT_FILE_PATH = Path.joinpath(TEMP_FOLDER_PATH, CAT_FILE_NAME)
