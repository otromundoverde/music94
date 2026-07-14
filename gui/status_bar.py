from PySide6.QtWidgets import QStatusBar


class Music94StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()

        self.showMessage("Estado: Listo")