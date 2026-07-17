from gui.metadata_reader import MetadataReader
from gui.importer import MusicImporter

importer = MusicImporter()

songs = importer.scan_folder(r"C:\Users\galli\Music")

reader = MetadataReader()

print()

for song in songs:

    data = reader.read(song)

    print("=" * 60)

    if data is None:

        print("No se pudo leer:", song)

    else:

        for key, value in data.items():

            print(f"{key:12}: {value}")

print()