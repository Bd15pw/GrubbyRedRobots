# Importujemy pathlib i zaczynamy prace z plikiem, ustawiamy sobie  root do scieżki root_dir, root_dir.iterdir() iteruje nam po plikach w folderze i pentlą sobie przechodzimy i zmieniamy nazwe pliku. Outputem jest zmiana nazwy pliku w folderze 


from pathlib import Path

root_dir= Path('files')

file_paths= root_dir.iterdir()

for path in file_paths:
  new_filename = "new-" + path.stem + path.suffix
  new_filepath = path.with_name(new_filename) # to powodouje ze zostajmy w folderze files
  path.rename(new_filepath)