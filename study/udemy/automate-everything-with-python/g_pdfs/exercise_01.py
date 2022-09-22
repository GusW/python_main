from pathlib import Path

import tabula

from g_pdfs.constants import EXERCISE_01_PDF_PATH, TEMP_FOLDER_PATH


def main():
    for idx, df in enumerate(tabula.read_pdf(EXERCISE_01_PDF_PATH, pages=1), 1):
        df.to_excel(
            Path.joinpath(TEMP_FOLDER_PATH, f"{EXERCISE_01_PDF_PATH.stem}_{idx}.xlsx"),
            index=None,
        )


if __name__ == "__main__":
    main()
