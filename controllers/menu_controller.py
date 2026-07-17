from PySide6.QtCore import QObject
from PySide6.QtWidgets import QFileDialog

from gui.importer import MusicImporter


class MenuController(QObject):

    def __init__(self, window):

        super().__init__()

        self.window = window

        self.importer = MusicImporter()

        self.connect_actions()

    # ---------------------------------------------------------
    # CONEXIONES
    # ---------------------------------------------------------

    def connect_actions(self):

        # Archivo

        self.window.action_new_project.triggered.connect(
            self.new_project
        )

        self.window.action_open_library.triggered.connect(
            self.open_library
        )

        self.window.action_save_library.triggered.connect(
            self.save_library
        )

        self.window.action_import_music.triggered.connect(
            self.import_music
        )

        self.window.action_import_folder.triggered.connect(
            self.import_folder
        )

        self.window.action_export_csv.triggered.connect(
            self.export_csv
        )

        self.window.action_export_excel.triggered.connect(
            self.export_excel
        )

        self.window.action_export_json.triggered.connect(
            self.export_json
        )

        # Biblioteca

        self.window.action_update_library.triggered.connect(
            self.update_library
        )

        self.window.action_find_duplicates.triggered.connect(
            self.find_duplicates
        )

        self.window.action_statistics.triggered.connect(
            self.statistics
        )

        # Spotify

        self.window.action_spotify_connect.triggered.connect(
            self.spotify_connect
        )

        self.window.action_spotify_sync.triggered.connect(
            self.spotify_sync
        )

        # Herramientas

        self.window.action_bpm.triggered.connect(
            self.analyze_bpm
        )

        self.window.action_key.triggered.connect(
            self.analyze_key
        )

    # =====================================================
    # ARCHIVO
    # =====================================================

    def new_project(self):

        self.window.statusBar().showMessage(
            "Nuevo proyecto",
            3000
        )

    def open_library(self):

        self.window.statusBar().showMessage(
            "Abrir biblioteca",
            3000
        )

    def save_library(self):

        self.window.statusBar().showMessage(
            "Guardar biblioteca",
            3000
        )

    def import_music(self):

        self.window.statusBar().showMessage(
            "Importar música",
            3000
        )

    def import_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self.window,
            "Seleccionar carpeta de música"
        )

        if not folder:
            return

        self.window.statusBar().showMessage(
            "Escaneando carpeta...",
            3000
        )

        library = self.importer.import_folder(folder)

        print()
        print("=" * 60)
        print("BIBLIOTECA IMPORTADA")
        print("=" * 60)

        print(f"Canciones encontradas: {len(library)}")

        for song in library[:10]:
            print(song)

        print("=" * 60)

        # ===========================================
        # ACTUALIZAR INTERFAZ
        # ===========================================

        self.window.content.load_library(library)

        self.window.statusBar().showMessage(
            f"{len(library)} canciones importadas",
            5000
        )

    def export_csv(self):

        self.window.statusBar().showMessage(
            "Exportar CSV",
            3000
        )

    def export_excel(self):

        self.window.statusBar().showMessage(
            "Exportar Excel",
            3000
        )

    def export_json(self):

        self.window.statusBar().showMessage(
            "Exportar JSON",
            3000
        )

    # =====================================================
    # BIBLIOTECA
    # =====================================================

    def update_library(self):

        self.window.statusBar().showMessage(
            "Actualizar biblioteca",
            3000
        )

    def find_duplicates(self):

        self.window.statusBar().showMessage(
            "Buscar duplicados",
            3000
        )

    def statistics(self):

        self.window.statusBar().showMessage(
            "Estadísticas",
            3000
        )

    # =====================================================
    # SPOTIFY
    # =====================================================

    def spotify_connect(self):

        self.window.statusBar().showMessage(
            "Conectar Spotify",
            3000
        )

    def spotify_sync(self):

        self.window.statusBar().showMessage(
            "Sincronizar Spotify",
            3000
        )

    # =====================================================
    # HERRAMIENTAS
    # =====================================================

    def analyze_bpm(self):

        self.window.statusBar().showMessage(
            "Analizando BPM",
            3000
        )

    def analyze_key(self):

        self.window.statusBar().showMessage(
            "Analizando tonalidad",
            3000
        )