from PySide6.QtCore import Qt

from PySide6.QtGui import QFont

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
)


class Header(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.title = QLabel("Inicio")

        self.title.setFont(
            QFont(
                "Segoe UI",
                20,
                QFont.Bold
            )
        )

        self.subtitle = QLabel(
            "Music94 • Analizador musical profesional"
        )

        self.subtitle.setAlignment(Qt.AlignLeft)

        layout.addWidget(self.title)

        layout.addWidget(self.subtitle)

        self.setLayout(layout)

    def set_page(self, page):

        page = page.strip()

        if page == "":
            return

        self.title.setText(page)