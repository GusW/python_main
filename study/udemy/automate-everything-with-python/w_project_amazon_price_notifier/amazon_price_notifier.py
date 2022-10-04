from datetime import datetime
from time import sleep
from typing import Optional

from bs4 import BeautifulSoup
import requests

from f_emails.constants import RECEIVER
from f_emails.send_gmail_email import send_email
from v_sms.constants import TWILIO_PHONE_NUMBER_DESTINATION
from v_sms.send_sms import send_sms

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157"
        + "Safari/537.36"
    ),
    "Accept-Language": "en-US, en;q=0.5",
}


def html_to_text(url: str) -> Optional[str]:
    return res.text if (res := requests.get(url, headers=HEADERS)) else ""


def extract_price_from_amazon_url(url: str) -> Optional[str]:
    content = html_to_text(url)
    soup = BeautifulSoup(content, "html.parser")
    if (
        (price_symbol := soup.find("span", class_="a-price-symbol"))
        and (price_whole := soup.find("span", class_="a-price-whole"))
        and (price_fraction := soup.find("span", class_="a-price-fraction"))
    ):
        return f"{price_symbol.get_text()} {price_whole.get_text()}{price_fraction.get_text()}"


def subscribe_to_price_changes_in(
    url: str,
    product_name: str,
    email_receiver: str = RECEIVER,
    sms_receiver: str = TWILIO_PHONE_NUMBER_DESTINATION,
    frequency_check_seconds: int = 60,
) -> None:
    product_price = ""
    while True:
        print(f"\n{datetime.utcnow()} Checking price of {product_name}...\n")
        price_from_url = extract_price_from_amazon_url(url)
        if product_price != price_from_url:
            product_price = price_from_url

            subject = f"{product_name} is now {product_price}"
            text = f"{subject} => {url}"

            send_email(email_receiver, subject, text)
            send_sms(sms_receiver, text)
        else:
            print(f"{datetime.utcnow()} No price changes.\n")

        sleep(frequency_check_seconds)


def main():
    url1 = "https://www.amazon.com/PF-WaterWorks-PF0989-Disposal-Installation/dp/B078H38Q1M/"
    subscribe_to_price_changes_in(
        url1, "PF WaterWorks PF0989 Garbage Disposal Installation Kit, White"
    )


if __name__ == "__main__":
    main()
