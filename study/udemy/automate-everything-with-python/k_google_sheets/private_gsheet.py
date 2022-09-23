import re

from k_google_sheets.config import get_gs
from k_google_sheets.constants import PRIVATE_GSHEET_NAME


def read_only():
    gs = get_gs()
    spreadsheet = gs.open(PRIVATE_GSHEET_NAME)

    # get worksheet by index
    worksheet1 = spreadsheet.get_worksheet(0)
    data1 = worksheet1.get_all_records()
    print(f"{data1=}\n")

    # get worksheet by name
    worksheet2 = spreadsheet.worksheet("2014")

    # get row data by cells
    data2_rows = worksheet2.get_values("A5:F7")
    print(f"{data2_rows=}\n")

    # get row data by index
    data2_rows = worksheet2.row_values(5)
    print(f"{data2_rows=}\n")

    # get col data by index
    data2_col = worksheet2.col_values(4)
    print(f"{data2_col=}\n")

    # get cell value
    cell1 = worksheet1.acell("D5").value
    print(f"{cell1=}\n")

    # search for a cell containing a value
    cell2 = worksheet1.find("9975")
    print(f"{cell2.row=}")
    print(f"{cell2.col=}\n")

    # search for all cells containing a value
    for cell in worksheet1.findall("-9"):
        print(f"{cell.col=}")
        print(f"{cell.row=}\n")

    # search by regex
    regex = re.compile(r"997")
    for regex_cell in worksheet1.findall(regex):
        print(f"{regex_cell.col=}")
        print(f"{regex_cell.row=}\n")


def update_cells():
    gs = get_gs()
    spreadsheet = gs.open(PRIVATE_GSHEET_NAME)

    worksheet1 = spreadsheet.worksheet("2013")

    # Update a cell
    worksheet1.update("E5", -292)

    # Update a cell based on row-column
    worksheet1.update_cell(5, 5, -29)

    # Update a column
    source = "E2:E25"
    target = "G1:G25"
    new_values = [
        [round(float(item) * 9 / 5 + 32, 1)]
        for sublist in worksheet1.get_values(source)
        for item in sublist
    ]
    worksheet1.update(target, [["Fahrenheit"], *new_values])


if __name__ == "__main__":
    # read_only()
    update_cells()
