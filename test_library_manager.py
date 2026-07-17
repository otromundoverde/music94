from gui.library_manager import LibraryManager

manager = LibraryManager()

library = manager.import_folder(
    r"C:\Users\galli\Music"
)

print()

print("=" * 60)

stats = manager.statistics()

print(stats)

print("=" * 60)

for song in manager.get_library():

    print(

        song["artist"],

        "-",

        song["title"]

    )