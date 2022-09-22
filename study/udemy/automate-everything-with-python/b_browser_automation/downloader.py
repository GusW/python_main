from pathlib import Path
from datetime import datetime
from time import mktime

import requests

from b_browser_automation.constants import (
    TEMP_FOLDER_PATH,
    USER_AGENT,
    YAHOO_FINANCE_URI,
    YAHOO_FINANCE_URI_SUFFIX,
)


def download_ticker_data(
    ticker_code: str = "GOOG",
    period_init: str = "1092873600",
    period_end: str = "1663545600",
    interval: str = "1d",  # 1 day
) -> bytes:
    period_init_params = f"?period1={period_init}"
    period_end_params = f"&period2={period_end}"
    interval_params = f"&interval={interval}"

    url = (
        f"{YAHOO_FINANCE_URI}{ticker_code}{period_init_params}{period_end_params}{interval_params}"
        + YAHOO_FINANCE_URI_SUFFIX
    )

    return requests.get(url, headers={"User-Agent": USER_AGENT}).content


def create_ticker_file(content: bytes, ticker_code: str = "GOOG") -> None:
    with open(Path.joinpath(TEMP_FOLDER_PATH, f"{ticker_code}.txt"), "wb") as f:
        f.write(content)


def _capture_date(target: str):
    date_obj = datetime.strptime(
        input(f"Enter {target} date in YYYY/MM/DD format: "), "%Y/%m/%d"
    )
    return int(mktime(date_obj.timetuple()))


if __name__ == "__main__":
    ticker_code = input("Enter the ticker symbol: ")
    period_init = _capture_date("start")
    period_end = _capture_date("end")

    create_ticker_file(
        download_ticker_data(
            ticker_code=ticker_code, period_init=period_init, period_end=period_end
        ),
        ticker_code=ticker_code,
    )
