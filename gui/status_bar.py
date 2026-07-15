from PySide6.QtWidgets import (
    QLabel,
    QStatusBar,
)


class Music94StatusBar(QStatusBar):

    def __init__(self):
        super().__init__()

        self.showMessage("Estado: Listo")

        self.library = QLabel("Biblioteca: 3 canciones")

        self.spotify = QLabel("Spotify: OFF")

        self.version = QLabel("Music94 v0.1")

        self.addPermanentWidget(self.library)

        self.addPermanentWidget(self.spotify)

        self.addPermanentWidget(self.version)