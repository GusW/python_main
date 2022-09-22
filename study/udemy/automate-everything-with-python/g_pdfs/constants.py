from pathlib import Path

PARENT_FOLDER = Path(__file__).parent.resolve()
TEMP_FOLDER_NAME = "temp"
TEMP_FOLDER_PATH = Path.joinpath(PARENT_FOLDER, TEMP_FOLDER_NAME)

EXCEL_FILE_PATH = Path.joinpath(TEMP_FOLDER_PATH, "data.xlsx")
EXERCISE_01_PDF_PATH = Path.joinpath(TEMP_FOLDER_PATH, "exercise_01.pdf")
PDF_IMAGE_PATH = Path.joinpath(TEMP_FOLDER_PATH, "tiger.jpeg")
STUDENTS_PDF_PATH = Path.joinpath(TEMP_FOLDER_PATH, "students.pdf")
WEATHER_PDF_PATH = Path.joinpath(TEMP_FOLDER_PATH, "weather.pdf")
