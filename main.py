"""
Ćwiczenie 1: Sumowanie liczb parzystych
Zadanie:
Napisz program, który sumuje wszystkie liczby parzyste od 1 do 100.

Objaśnienie:
Utwórz zmienną, która będzie przechowywać sumę liczb parzystych (np. sum_even).
Użyj pętli for, aby przejść przez liczby od 1 do 100.
W każdej iteracji sprawdź, czy liczba jest parzysta (podzielna przez 2 bez reszty).
Jeśli liczba jest parzysta, dodaj ją do zmiennej sum_even.
Po zakończeniu pętli wypisz wartość zmiennej sum_even.
"""

sum_even = 0 

for i in range(101):
  if i % 2 == 0: 
    sum_even += i 

print(sum_even)

"""
Ćwiczenie 2: Wypisywanie liczb podzielnych przez 3
Zadanie:
Napisz program, który wypisuje wszystkie liczby od 1 do 50, które są podzielne przez 3.
Objaśnienie:
Użyj pętli for, aby przejść przez liczby od 1 do 50.
W każdej iteracji sprawdź, czy liczba jest podzielna przez 3 (reszta z dzielenia przez 3 wynosi 0).
Jeśli liczba jest podzielna przez 3, wypisz ją.


"""
print("--------------------ZADANIE 2----------------")
list =[] 

for i in range(1,50): 
  if i %3==0: 
    list.append(i)

print(list)

print("--------------------ZADANIE 3----------------")

"""
Ćwiczenie 3: Znajdowanie maksymalnej liczby
Zadanie:
Napisz program, który z listy liczb znajdzie i wypisze największą liczbę.
Objaśnienie:
Utwórz listę z kilkoma liczbami (np. numbers = [3, 7, 2, 10, 15, 1, 9]).
Utwórz zmienną, która będzie przechowywać największą liczbę (np. max_number) i ustaw jej początkową wartość na pierwszy element listy.
Użyj pętli for, aby przejść przez wszystkie liczby w liście.
W każdej iteracji porównaj aktualną liczbę z wartością w zmiennej max_number.
Jeśli aktualna liczba jest większa niż wartość w max_number, zaktualizuj max_number do tej liczby.
Po zakończeniu pętli wypisz wartość zmiennej max_number.
Powodzenia w rozwiązywaniu zadań! Jeśli będziesz potrzebować pomocy, chętnie pomogę.
"""


numbers=[3, 7, 2, 10, 15, 1, 9]

max_numer = numbers[0]

for i in numbers:
  if i > max_numer: 
    max_numer = i 


print(max_numer)



