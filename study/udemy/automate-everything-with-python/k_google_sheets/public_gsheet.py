from pandas import read_csv

from k_google_sheets.constants import PUBLIC_GSHEET_2013_URI, PUBLIC_GSHEET_2014_URI


def read_only():
    data_2013 = read_csv(PUBLIC_GSHEET_2013_URI)
    print(f"{data_2013=}")

    data_2014 = read_csv(PUBLIC_GSHEET_2014_URI)
    print(f"{data_2014=}")


if __name__ == "__main__":
    read_only()
