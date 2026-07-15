from PySide6.QtCore import Signal

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QHBoxLayout,
    QComboBox,
)


class FilterBar(QWidget):

    filtersChanged = Signal()

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout()

        self.genre = QComboBox()

        self.genre.addItems([
            "Todos los géneros",
            "House",
            "IDM",
            "Trip Hop",
        ])

        self.decade = QComboBox()

        self.decade.addItems([
            "Todos los años",
            "1970s",
            "1980s",
            "1990s",
            "2000s",
        ])

        self.order = QComboBox()

        self.order.addItems([
            "Ordenar por",
            "Título",
            "Artista",
            "Álbum",
            "Año",
        ])

        layout.addWidget(QLabel("Género"))

        layout.addWidget(self.genre)

        layout.addSpacing(15)

        layout.addWidget(QLabel("Década"))

        layout.addWidget(self.decade)

        layout.addSpacing(15)

        layout.addWidget(QLabel("Orden"))

        layout.addWidget(self.order)

        layout.addStretch()

        self.setLayout(layout)

        self.genre.currentIndexChanged.connect(
            self.filtersChanged.emit
        )

        self.decade.currentIndexChanged.connect(
            self.filtersChanged.emit
        )

        self.order.currentIndexChanged.connect(
            self.filtersChanged.emit
        )