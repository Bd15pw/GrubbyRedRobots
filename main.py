from pathlib import Path

p1 = Path('files/abc.txt')

with open(p1, 'r') as file:
  print(file.read())