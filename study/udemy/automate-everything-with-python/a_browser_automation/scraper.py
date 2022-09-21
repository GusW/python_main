from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from a_browser_automation.config import get_driver


TITLE_XPATH = "/html/body/div[1]/div/h1[1]"
DYNAMIC_CONTENT_XPATH = "/html/body/div[1]/div/h1[2]"


def clean_temp_text(text: str) -> str:
    return float(temp) if (temp := text.split(":")[-1]) else 0.0


def get_dynamic_content(driver: Chrome) -> None:
    sleep(2)  # content takes around 2 seconds to be rendered on screen
    dynamic_content = driver.find_element(By.XPATH, DYNAMIC_CONTENT_XPATH)
    print(f"{dynamic_content.text=}\n")
    temperature = clean_temp_text(dynamic_content.text)
    print(f"{temperature=}\n")
    return temperature


def main():
    driver = get_driver()
    page_title = driver.find_element(By.XPATH, TITLE_XPATH)
    print(f"{page_title.text=}\n")

    get_dynamic_content(driver)
    return driver


if __name__ == "__main__":
    driver = main()
    driver.close()
