def funkcja(**czlonkowie): 
  for typ, imie in czlonkowie.items():
    print(typ, "->", imie)

funkcja(mama="Grażyna", tata="Andrzej")