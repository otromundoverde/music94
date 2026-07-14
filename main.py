import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import Music94


app = QApplication(sys.argv)

window = Music94()
window.show()

sys.exit(app.exec())