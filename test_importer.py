from gui.importer import MusicImporter

importer = MusicImporter()

library = importer.import_folder(
    r"C:\Users\galli\Music"
)

print()

print("=" * 60)

print("Canciones importadas:", importer.total_songs())

print("=" * 60)

for song in library:

    print()

    print(song["title"])

    print(song["artist"])

    print(song["album"])

    print(song["year"])

    print(song["genre"])

    print(song["duration"])

    print(song["bitrate"], "kbps")