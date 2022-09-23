from pathlib import Path

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)
from PyQt6.QtCore import Qt

from e_files_and_folders.safe_delete import safe_delete


def safe_delete_manager():
    file_full_paths = []

    def _open_file_dialog():
        nonlocal file_full_paths
        file_full_paths, _ = QFileDialog.getOpenFileNames(window, "Select Files")

    def _safe_delete_files():
        log_messages.setText("")
        logs = ""
        for full_path in file_full_paths:
            file_path = Path(full_path)
            logs += f"Cleaning and removing {file_path.name}\n"
            log_messages.setText(logs)
            safe_delete(file_path)

    # Boilerplate
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Safe Delete Manager")

    # Main Layout
    layout = QVBoxLayout()

    description = QLabel(
        "Select the files you want to safely delete."
        + "The files will be <b><font color='red'>permanently</font></b> removed."
    )
    layout.addWidget(description)

    # Open file dialog button
    open_btn = QPushButton("Select files")
    layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    open_btn.setToolTip("Select multiple files to be removed")
    open_btn.setFixedWidth(200)
    open_btn.clicked.connect(_open_file_dialog)

    # Delete action button
    delete_btn = QPushButton("Safe delete")
    layout.addWidget(delete_btn, alignment=Qt.AlignmentFlag.AlignCenter)
    delete_btn.setToolTip("Cleanup and delete files")
    delete_btn.setFixedWidth(200)
    delete_btn.clicked.connect(_safe_delete_files)

    # Open file dialog button
    log_messages = QLabel("")
    layout.addWidget(log_messages)

    # Boilerplate
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    safe_delete_manager()
