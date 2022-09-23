from time import sleep

from k_google_sheets.config import get_gs
from k_google_sheets.constants import PRIVATE_GSHEET_NAME


def listen_to_changes():
    gs = get_gs()
    spreadsheet = gs.open(PRIVATE_GSHEET_NAME)

    worksheet1 = spreadsheet.worksheet("2013")
    worksheet2 = spreadsheet.worksheet("watch")

    while True:
        value1 = worksheet1.acell("G26").value
        sleep(2)
        value2 = worksheet1.acell("G26").value
        if value1 != value2:
            worksheet2.update("A1", f"Changed: {value2}")


if __name__ == "__main__":
    listen_to_changes()
