from PySide6.QtWidgets import QWidget, QVBoxLayout

from gui.header import Header
from gui.library_table import LibraryTable


class ContentPanel(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.addWidget(Header())

        layout.addWidget(LibraryTable())

        self.setLayout(layout)