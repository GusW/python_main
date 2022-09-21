from pathlib import Path

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.chrome.service import Service

from c_stock_percentage_scraper.constants import ZSE_URI

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
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    return options


def get_driver(url: str = ZSE_URI):
    options = _create_options()
    driver = Chrome(service=service, options=options)
    driver.minimize_window()
    driver.get(url)
    return driver
