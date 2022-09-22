from fpdf import FPDF
from pathlib import Path
import pandas as pd

from g_pdfs.constants import EXCEL_FILE_PATH, TEMP_FOLDER_PATH


def main():
    df = pd.read_excel(EXCEL_FILE_PATH)
    for _, row in df.iterrows():
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # name
        pdf.set_font(family="Arial", style="B", size=24)
        pdf.cell(w=0, h=50, txt=row["name"], align="C", ln=1)

        for col in df.columns[1:]:
            pdf.set_font(family="Arial", style="B", size=14)
            pdf.cell(w=100, h=25, txt=f"{col.title()}:")

            pdf.set_font(family="Arial", size=14)
            pdf.cell(w=100, h=25, txt=row[col], ln=1)

        pdf.output(Path.joinpath(TEMP_FOLDER_PATH, f"{row['name']}.pdf").as_posix())


if __name__ == "__main__":
    main()
