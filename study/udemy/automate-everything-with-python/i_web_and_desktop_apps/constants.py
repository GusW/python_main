from pathlib import Path


PARENT_FOLDER_PATH = Path(__file__).parent.resolve()
TEMPLATE_FOLDER_NAME = "templates"
TEMPLATE_FOLDER_PATH = Path.joinpath(PARENT_FOLDER_PATH, TEMPLATE_FOLDER_NAME)

INDEX_HTML_NAME = "index.html"
INDEX_HTML_PATH = Path.joinpath(TEMPLATE_FOLDER_PATH, INDEX_HTML_NAME)
