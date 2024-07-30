#list =[1,15,13,35]

#user = int(input("Podaj liczbę: "))

#print(user in list)

lista=[2,2,4,5,6,22,2,3,3,1,1,5,6,4,4,3,5]

#print(lista.count(2))

unilakne_liczby=[]

for liczba in lista: 
  if liczba not in unilakne_liczby:
    unilakne_liczby.append(liczba)

print(unilakne_liczby)


