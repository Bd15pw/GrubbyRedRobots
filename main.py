def dodaj(*args):
  suma = 0
  for liczba in args:
    suma += liczba
  print(suma)
dodaj(10,15,14)