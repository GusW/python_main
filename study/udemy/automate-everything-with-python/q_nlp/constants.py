from pathlib import Path

TEMP_FOLDER_NAME = "temp"
SENTENCES_SAMPLE_FILE_NAME = "sentences.txt"


PARENT_FOLDER_PATH = Path(__file__).parent.resolve()

TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMP_FOLDER_NAME)

SENTENCES_SAMPLE_PATH = Path.joinpath(TEMP_FOLDER_PATH, SENTENCES_SAMPLE_FILE_NAME)
