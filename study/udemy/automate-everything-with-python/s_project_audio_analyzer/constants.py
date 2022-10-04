from pathlib import Path

TEMP_FOLDER_NAME = "temp"
AUDIO_FILE_NAME = "chile.wav"

PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

AUDIO_FILE_PATH = Path.joinpath(TEMP_FOLDER_PATH, AUDIO_FILE_NAME)
