from functools import cache
from pathlib import Path
from pprint import pprint
from typing import Optional
import sqlite3

from fpdf import FPDF
import pandas as pd

from u_sql_databases.constants import DATABASE_PATH, TEMP_FOLDER_PATH

TABLE_NAME = "ips"


@cache
def _connect_to_db():
    return sqlite3.connect(DATABASE_PATH)


@cache
def _get_cursor():
    connection = _connect_to_db()
    return connection.cursor()


def get_ips(
    address: Optional[str] = "", domain: Optional[str] = "", asn: Optional[str] = ""
):
    cursor = _get_cursor()
    statement = f"SELECT * from '{TABLE_NAME}'"
    if address or domain or asn:
        statement = f"{statement} WHERE"
        if address:
            statement = f"{statement} address = '{address}'"
        if domain:
            statement = f"{statement} domain = '{domain}'"
        if asn:
            statement = f"{statement} asn = '{asn}'"

    cursor.execute(statement)
    return cursor.fetchall()


def _get_dataframe():
    connection = _connect_to_db()
    return pd.read_sql_query(f"SELECT * from '{TABLE_NAME}' ORDER BY asn", connection)


def sql_to_csv(target_file_path: Path):
    df = _get_dataframe()
    # index=None removes first col in csv (index)
    df.to_csv(target_file_path, index=None)


def sql_to_excel(target_file_path: Path):
    df = _get_dataframe()
    # index=None removes first col in xls (index)
    df.to_excel(target_file_path, index=None)


def _get_table_cols():
    cursor = _get_cursor()
    cursor.execute(f"PRAGMA table_info({TABLE_NAME})")
    cols = cursor.fetchall()
    # [(idx, col_name, col_type, ...)]
    return [col[1] for col in cols]


def _get_table_rows():
    cursor = _get_cursor()
    cursor.execute(f"SELECT * from '{TABLE_NAME}'")
    return cursor.fetchall()


def sql_to_pdf(target_file_path: Path):
    pdf = FPDF(orientation="P", unit="pt", format="A4")
    pdf.add_page()
    for col in _get_table_cols():
        pdf.set_font(family="Times", style="B", size=14)
        pdf.cell(w=100, h=30, txt=col, border=1)

    pdf.ln()
    for row in _get_table_rows():
        for item in row:
            pdf.set_font(family="Times", size=12)
            pdf.cell(w=100, h=30, txt=str(item), border=1)
        pdf.ln()

    pdf.output(target_file_path)


def insert_ips(ip_list: list[tuple[str, str, int]]) -> None:
    connection = _connect_to_db()
    cursor = _get_cursor()

    cursor.executemany(f"INSERT INTO {TABLE_NAME} VALUES(?,?,?)", ip_list)
    connection.commit()


def main():
    print("\n")
    pprint(get_ips())
    print("\n")
    pprint(get_ips(asn=330))
    print("\n")
    pprint(get_ips(domain="whatever"))

    sql_to_csv(Path.joinpath(TEMP_FOLDER_PATH, "database.csv"))

    sql_to_excel(Path.joinpath(TEMP_FOLDER_PATH, "database.xlsx"))

    sql_to_pdf(Path.joinpath(TEMP_FOLDER_PATH, "database.pdf"))

    new_ips = [
        ("010.101.010.101", "whatever.com", 897),
        ("010.202.010.101", "whatever.se", 777),
    ]
    insert_ips(new_ips)
    pprint(get_ips())


if __name__ == "__main__":
    main()
