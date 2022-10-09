from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
)

from zc_miscellaneous.dictionary import define


def english_dict_desktop_app():
    def _find_definition():
        input_text = text.text()
        output_label.setText("\n".join(define(input_text)))

    # Boilerplate
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Word Definition")

    # Main Layout
    layout = QVBoxLayout()

    # Content Layout
    layout_content = QHBoxLayout()
    layout.addLayout(layout_content)

    text = QLineEdit()
    layout_content.addWidget(text)

    btn = QPushButton("Find")
    layout_content.addWidget(btn)
    btn.clicked.connect(_find_definition)

    # Result/Output Layout
    output_label = QLabel("")
    layout.addWidget(output_label)

    # Boilerplate
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    english_dict_desktop_app()
