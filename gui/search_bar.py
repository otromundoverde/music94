from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QLineEdit,
)


class SearchBar(QWidget):

    searchChanged = Signal(str)

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()

        layout.addWidget(QLabel("Buscar"))

        self.box = QLineEdit()

        self.box.setPlaceholderText(
            "Canción, artista, álbum..."
        )

        layout.addWidget(self.box)

        self.box.textChanged.connect(
            self.searchChanged.emit
        )

        self.setLayout(layout)