from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

from b_browser_automation.scraper_bs4 import main as converter

CURRENCIES = ["USD", "EUR", "GBP", "CHF", "SEK", "BRL", "ARS"]


def multiple_converter():
    def _show_ccy():
        input_text = float(text.text() or 1)
        in_ccy = in_combo.currentText()
        out_ccy = out_combo.currentText()
        converted = converter(in_ccy, out_ccy, input_text)
        output_label.setText(f"{in_ccy} {input_text} : {converted} {out_ccy}")

    # Boilerplate
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("CCY converter")

    # Main Layout
    layout = QVBoxLayout()

    # Content Layout
    layout_content = QHBoxLayout()
    layout.addLayout(layout_content)

    # Result/Output Layout
    output_label = QLabel("")
    layout.addWidget(output_label)

    # Content - Comboboxes
    layout_comboboxes = QVBoxLayout()
    layout_content.addLayout(layout_comboboxes)

    in_combo = QComboBox()
    in_combo.addItems(CURRENCIES)
    layout_comboboxes.addWidget(in_combo)

    out_combo = QComboBox()
    out_combo.addItems(CURRENCIES)
    layout_comboboxes.addWidget(out_combo)

    # Content - Comboboxes
    layout_input = QVBoxLayout()
    layout_content.addLayout(layout_input)

    text = QLineEdit()
    layout_input.addWidget(text)

    btn = QPushButton("Convert")
    layout_input.addWidget(btn)
    btn.clicked.connect(_show_ccy)

    # Boilerplate
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    multiple_converter()
