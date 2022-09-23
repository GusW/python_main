from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from b_browser_automation.scraper_bs4 import main as converter


def simple_app():
    def _make_sentence():
        input_text = text.text()
        output_label.setText(f"{input_text.capitalize()}.")

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Sentence Maker")

    layout = QVBoxLayout()

    text = QLineEdit()
    layout.addWidget(text)

    btn = QPushButton("Make")
    layout.addWidget(btn)

    btn.clicked.connect(_make_sentence)

    output_label = QLabel("")
    layout.addWidget(output_label)

    window.setLayout(layout)
    window.show()
    app.exec()


def simple_converter():
    def _show_ccy():
        input_text = float(text.text() or 1)
        converted = converter("USD", "EUR", input_text)
        output_label.setText(f"USD {input_text} : {converted} EUR")

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("USD/EUR converter")

    layout = QVBoxLayout()

    text = QLineEdit()
    layout.addWidget(text)

    btn = QPushButton("Convert")
    layout.addWidget(btn)

    btn.clicked.connect(_show_ccy)

    output_label = QLabel("")
    layout.addWidget(output_label)

    window.setLayout(layout)
    window.show()
    app.exec()


def multiple_converter():
    def _show_ccy():
        input_text = float(text.text() or 1)
        in_ccy = in_combo.currentText()
        out_ccy = out_combo.currentText()
        converted = converter(in_ccy, out_ccy, input_text)
        output_label.setText(f"{in_ccy} {input_text} : {converted} {out_ccy}")

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("CCY converter")

    layout = QVBoxLayout()

    text = QLineEdit()
    layout.addWidget(text)

    currencies = ["USD", "EUR", "GBP", "CHF", "SEK", "BRL", "ARS"]

    in_combo = QComboBox()
    in_combo.addItems(currencies)
    layout.addWidget(in_combo)

    out_combo = QComboBox()
    out_combo.addItems(currencies)
    layout.addWidget(out_combo)

    btn = QPushButton("Convert")
    layout.addWidget(btn)

    btn.clicked.connect(_show_ccy)

    output_label = QLabel("")
    layout.addWidget(output_label)

    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    # simple_app()
    # simple_converter()
    multiple_converter()
