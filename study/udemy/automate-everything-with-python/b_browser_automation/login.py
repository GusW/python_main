from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from b_browser_automation.config import get_driver

_USERNAME = "automated"
_PASSWORD = "automatedautomated"


def main():
    driver = get_driver("http://automated.pythonanywhere.com/login/")
    driver.find_element(By.ID, "id_username").send_keys(_USERNAME)
    driver.find_element(By.ID, "id_password").send_keys(_PASSWORD + Keys.RETURN)
    print(f"{driver.current_url=}\n")

    driver.find_element(By.XPATH, "/html/body/nav/div/a").click()
    print(f"{driver.current_url=}\n")
    return driver


if __name__ == "__main__":
    driver = main()
    driver.close()
