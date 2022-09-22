from b_browser_automation.login import main as login
from b_browser_automation.scraper import get_dynamic_content


def main():
    driver = login()
    get_dynamic_content(driver)
    driver.close()


if __name__ == "__main__":
    main()
