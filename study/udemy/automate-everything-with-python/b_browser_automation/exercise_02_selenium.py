from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Callable

from selenium.webdriver import Chrome

from b_browser_automation.config import get_driver
from b_browser_automation.constants import TEMP_FOLDER_PATH
from b_browser_automation.scraper import get_dynamic_content


def set_timeout(callback_fn: Callable, timeout: int = 2):
    while True:
        callback_fn()
        sleep(timeout)


def handle_file(content: str):
    filename = f'{datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
    with open(Path.joinpath(TEMP_FOLDER_PATH, filename), "w") as f:
        f.write(content)


def write_temp_to_file(driver: Chrome):
    def closure():
        curr_temp = get_dynamic_content(driver)
        handle_file(str(curr_temp))

    return closure


def main():
    driver = get_driver()
    callback_fn = write_temp_to_file(driver)
    set_timeout(callback_fn, 2)


if __name__ == "__main__":
    main()
