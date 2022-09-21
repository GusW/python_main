from datetime import datetime
from pathlib import Path
from time import sleep
from typing import Callable

from selenium.webdriver.common.by import By

from c_stock_percentage_scraper.config import get_driver
from c_stock_percentage_scraper.constants import (
    STOCK_PERCENTAGE_FILE_NAME,
    TEMP_FOLDER_PATH,
)


STOCK_PERCENTAGE_XPATH = '//*[@id="app_indeks"]/section[1]/div/div/div[2]/span'


def clean_temp_text(text: str) -> str:
    return percentage if (percentage := text.split(" ")[0]) else "0.0"


def set_timeout_callback(callback_fn: Callable, timeout_in_seconds: int = 1) -> None:
    while True:
        callback_fn()
        sleep(timeout_in_seconds)


def persist_percentage_value(stringyfied_value: str) -> None:
    with open(Path.joinpath(TEMP_FOLDER_PATH, STOCK_PERCENTAGE_FILE_NAME), "a") as f:
        f.write(
            f"{datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')}\t{stringyfied_value}\n"
        )


def scraper_callback():
    try:
        driver = get_driver()
        sleep(5)
        if (
            stock_percentage := driver.find_element(By.XPATH, STOCK_PERCENTAGE_XPATH)
        ) and (target_percentage := stock_percentage.text):
            print(f"{target_percentage=}\n")
            persist_percentage_value(target_percentage)
    except Exception as err:
        print(f"Error while trying to scrape URI: {err}")
    finally:
        driver.close()


def main():
    set_timeout_callback(scraper_callback, 10)


if __name__ == "__main__":
    main()
