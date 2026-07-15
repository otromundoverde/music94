from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class Header(QWidget):

    def __init__(self):
        super().__init__()

        titulo = QLabel("Music94")
        titulo.setFont(QFont("Segoe UI", 16, QFont.Bold))

        subtitulo = QLabel("Organizador avanzado de bibliotecas musicales")

        layout = QVBoxLayout()

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)