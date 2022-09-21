from functools import lru_cache
from pathlib import Path

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service


ROOT_FOLDER = Path(__file__).parent.parent
RESOURCES_FOLDER_NAME = "resources"
CHROME_DRIVER_FILENAME = "chromedriver"
CHROME_DRIVER_PATH = Path.joinpath(
    ROOT_FOLDER, RESOURCES_FOLDER_NAME, CHROME_DRIVER_FILENAME
)
service = Service(CHROME_DRIVER_PATH)


def _create_options() -> ChromeOptions:
    options = ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    return options


@lru_cache(2)
def get_driver(url: str = "http://automated.pythonanywhere.com"):
    options = _create_options()
    driver = Chrome(service=service, options=options)
    driver.get(url)
    return driver
