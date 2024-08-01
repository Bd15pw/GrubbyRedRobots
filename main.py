def kantor(*kwoty,kurs=4.20):
  lista_kwot=[]
  for kwota in kwoty: 
    wymiana= round(kwota/ kurs, 2)
    lista_kwot.append(wymiana)
  return lista_kwot
  
wymianka = kantor(40,10,50,10,20,22,1,21,23)
plik = open("kantor.txt", "w")

for kwota in wymianka:
  plik.write(str(kwota) + "\n")
