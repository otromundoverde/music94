from PySide6.QtWidgets import QListWidget


class NavigationPanel(QListWidget):

    def __init__(self):
        super().__init__()

        self.addItem("🏠 Inicio")
        self.addItem("🎵 Biblioteca")
        self.addItem("👤 Artistas")
        self.addItem("💿 Álbumes")
        self.addItem("🎼 Géneros")
        self.addItem("📅 Años")
        self.addItem("⭐ Favoritos")
        self.addItem("📈 Estadísticas")
        self.addItem("🔎 Buscar")
        self.addItem("⚙ Configuración")