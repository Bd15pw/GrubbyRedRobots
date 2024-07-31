"""
Zadanie 1: Liczby Parzyste i Nieparzyste
Napisz program, który poprosi użytkownika o podanie liczby n, a następnie wyświetli wszystkie liczby od 1 do n. Dla każdej liczby, program powinien wskazać, czy jest parzysta, czy nieparzysta.

Wskazówki:

Użyj pętli for lub while do iteracji przez liczby od 1 do n.
Użyj instrukcji if-else do sprawdzenia, czy liczba jest parzysta (liczba % 2 == 0), czy nieparzysta.
Zadanie 2: Suma Liczb
Napisz program, który poprosi użytkownika o podanie liczby n, a następnie obliczy sumę wszystkich liczb od 1 do n.

Wskazówki:

Użyj pętli for lub while do iteracji przez liczby od 1 do n.
Zsumuj te liczby wewnątrz pętli.
Zadanie 3: Odwracanie Ciągu
Napisz program, który poprosi użytkownika o podanie ciągu znaków, a następnie wyświetli ten ciąg w odwrotnej kolejności.

Wskazówki:

Użyj pętli for do iteracji przez ciąg znaków od końca do początku.
Twórz nowy ciąg znaków, dodając kolejne litery w odwrotnej kolejności.
Zadanie 4: Liczby Pierwsze
Napisz program, który znajdzie wszystkie liczby pierwsze w zakresie od 1 do n, gdzie n jest podane przez użytkownika.

Wskazówki:

Użyj podwójnej pętli: zewnętrzna pętla for lub while do iteracji przez liczby od 2 do n.
Wewnętrzna pętla (lub dodatkowa logika) sprawdzi, czy dana liczba ma jakichkolwiek dzielników poza 1 i sobą (czyli sprawdzi, czy jest pierwsza).
Użyj instrukcji if-else, aby określić i wyświetlić liczby pierwsze.
Powodzenia w programowaniu! Jeśli napotkasz problemy, zawsze możesz wrócić i zadać pytania lub prosić o wskazówki.



"""

"""
Zadanie 1: Liczby Parzyste i Nieparzyste
Napisz program, który poprosi użytkownika o podanie liczby n, a następnie wyświetli wszystkie liczby od 1 do n. Dla każdej liczby, program powinien wskazać, czy jest parzysta, czy nieparzysta.

Wskazówki:

Użyj pętli for lub while do iteracji przez liczby od 1 do n.
Użyj instrukcji if-else do sprawdzenia, czy liczba jest parzysta (liczba % 2 == 0), czy nieparzysta.
"""

n = int(input("Wprowadź liczbę: "))
list=[]

i= 1
while i <= n:  
  print(i)
  if i%2==0:
    list.append(i)
  i += 1

print(list)

print("____________ Zadanie 2______________")

"""
Zadanie 2: Suma Liczb
Napisz program, który poprosi użytkownika o podanie liczby n, a następnie obliczy sumę wszystkich liczb od 1 do n.

Wskazówki:

Użyj pętli for lub while do iteracji przez liczby od 1 do n.
Zsumuj te liczby wewnątrz pętli.

"""

liczba = int(input("Wprowadź liczbę: "))

Zbiór = []
i = 0
while i <= liczba:
  Zbiór.append(i)
  i +=1 


suma = 0

for el in Zbiór: 
    suma += el 

Zbiór.reverse()

print(Zbiór)

print(suma)
