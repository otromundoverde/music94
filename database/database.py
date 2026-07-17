from pathlib import Path
import sqlite3

from database.schema import create_schema


class Database:

    def __init__(self):

        project_root = Path(__file__).resolve().parent.parent

        self.database_path = project_root / "music94.db"

        self.connection = sqlite3.connect(self.database_path)

        self.connection.row_factory = sqlite3.Row

        create_schema(self.connection)

    # ---------------------------------------------------------

    def cursor(self):

        return self.connection.cursor()

    # ---------------------------------------------------------

    def commit(self):

        self.connection.commit()

    # ---------------------------------------------------------

    def close(self):

        self.connection.close()