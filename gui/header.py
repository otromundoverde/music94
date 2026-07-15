from PySide6.QtCore import Qt

from PySide6.QtGui import QFont

from PySide6.QtWidgets import QLabel
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QWidget


class Header(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel("Biblioteca")

        self.title.setAlignment(Qt.AlignLeft)

        self.title.setFont(QFont("Tahoma", 18))

        self.subtitle = QLabel(
            "Music94 · Organizador musical y analizador de biblioteca"
        )

        self.subtitle.setFont(QFont("Tahoma", 9))

        layout = QVBoxLayout()

        layout.addWidget(self.title)

        layout.addWidget(self.subtitle)

        self.setLayout(layout)

    def set_page(self, page):

        self.title.setText(page)