from typing import Optional

from bs4 import BeautifulSoup
import requests

from a_browser_automation.constants import X_RATES_CALCULATOR_URI


def get_html(in_ccy: str, out_ccy: str, amount: int = 1) -> Optional[str]:
    url = f"{X_RATES_CALCULATOR_URI}?from={in_ccy}&to={out_ccy}&amount={amount}"
    return res.text if (res := requests.get(url)) else ""


def extract_fx_rate_from_html(content: str) -> Optional[str]:
    soup = BeautifulSoup(content, "html.parser")
    if fx_rate_html := soup.find("span", class_="ccOutputRslt"):
        return fx_rate_html.get_text()


def main(in_ccy: str, out_ccy: str, amount: int = 1) -> Optional[str]:
    html = get_html(in_ccy, out_ccy, amount)
    if html and (fx_rate := extract_fx_rate_from_html(html)):
        rate, ccy = fx_rate.split(" ")
        print(f"{ccy=}")
        print(f"{rate=}")

        return fx_rate


if __name__ == "__main__":
    main("USD", "SEK")
