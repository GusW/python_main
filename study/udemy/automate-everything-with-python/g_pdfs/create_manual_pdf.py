from datetime import datetime
from fpdf import FPDF
from pathlib import Path

from g_pdfs.constants import PDF_IMAGE_PATH, TEMP_FOLDER_PATH


def main():
    pdf = FPDF(orientation="P", unit="pt", format="A4")
    pdf.add_page()

    pdf.image(PDF_IMAGE_PATH.as_posix(), w=80, h=50)

    pdf.set_font(family="Arial", style="B", size=24)
    pdf.cell(w=0, h=50, txt="Malayan tiger", align="C", border=1, ln=1)

    pdf.set_font(family="Arial", style="B", size=14)
    pdf.cell(w=0, h=30, txt="Description", align="C", ln=1)

    pdf.set_font(family="Arial", size=12)
    description = (
        "The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies "
        + "that is native to The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris "
        + "subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts "
        + "of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015.\n"
        + "As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous "
        + "declining trend."
    )
    pdf.multi_cell(w=0, h=15, txt=description, align="L")

    pdf.set_font(family="Arial", style="B", size=14)
    pdf.cell(w=100, h=25, txt="Kingdom:")

    pdf.set_font(family="Arial", size=14)
    pdf.cell(w=100, h=25, txt="Animalia", ln=1)

    pdf.set_font(family="Arial", style="B", size=14)
    pdf.cell(w=100, h=25, txt="Phylum:")

    pdf.set_font(family="Arial", size=14)
    pdf.cell(w=100, h=25, txt="Chordata", ln=1)

    pdf.output(
        Path.joinpath(
            TEMP_FOLDER_PATH, f"{datetime.utcnow().timestamp()}.pdf"
        ).as_posix()
    )


if __name__ == "__main__":
    main()
