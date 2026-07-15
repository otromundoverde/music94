from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QListWidget,
)


class NavigationPanel(QListWidget):

    page_selected = Signal(str)

    def __init__(self):

        super().__init__()

        self.addItems(

            [

                "Biblioteca",

                "Artistas",

                "Álbumes",

                "Géneros",

                "Décadas",

                "Favoritos",

            ]

        )

        self.setCurrentRow(0)

        self.currentTextChanged.connect(
            self.page_selected.emit
        )