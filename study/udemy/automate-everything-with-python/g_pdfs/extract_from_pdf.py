from pathlib import Path, PosixPath

import fitz
import tabula

from g_pdfs.constants import STUDENTS_PDF_PATH, WEATHER_PDF_PATH, TEMP_FOLDER_PATH


def extract_pdf_pages_text(pdf_path: PosixPath):
    with fitz.open(pdf_path) as pdf:
        for idx, page in enumerate(pdf, 1):
            print(f"Page: {idx} {'-' * 20}", "\n", page.get_text(), "\n\n")


def extract_tables_from_pdf(pdf_path: PosixPath):
    table = tabula.read_pdf(pdf_path, pages=1)
    print(f"{table=}")
    # table = list[data_frames]
    # export as csv:
    for idx, df in enumerate(table, 1):
        df.to_csv(
            Path.joinpath(TEMP_FOLDER_PATH, f"{pdf_path.stem}_{idx}.csv"), index=None
        )


def main():
    # extract_pdf_pages_text

    extract_pdf_pages_text(STUDENTS_PDF_PATH)

    # extract_pdf_pages_text
    # extract_tables_from_pdf

    extract_tables_from_pdf(WEATHER_PDF_PATH)

    # extract_tables_from_pdf


if __name__ == "__main__":
    main()
