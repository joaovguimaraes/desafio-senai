a = input('informe 2 numeros: ')
print(a)

lista = list(a)
print(lista)

index=0

for x in lista:
    
  repeticoes = lista.count(lista[index])
  sapo = [str(repeticoes),lista[index]]
  print(sapo)
  index+=1
  sapo=[sapo[lista],]