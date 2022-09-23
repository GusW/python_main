from statistics import mean

from k_google_sheets.config import get_gs
from k_google_sheets.constants import PRIVATE_GSHEET_NAME


def calculate_temp_mean():
    gs = get_gs()
    spreadsheet = gs.open(PRIVATE_GSHEET_NAME)

    worksheet1 = spreadsheet.worksheet("2013")

    # Update a column
    source = "G2:G25"
    target = "G26"
    mean_temp = mean(
        [float(item) for sublist in worksheet1.get_values(source) for item in sublist]
    )
    worksheet1.update(target, mean_temp)


if __name__ == "__main__":
    calculate_temp_mean()
