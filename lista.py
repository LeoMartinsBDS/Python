minha_lista = ["a", "b", "c"]
minha_lista2 = [1,2,20,50,80, 100,3 , 900]

minha_lista.append("d")


minha_lista2.reverse()
print(minha_lista2)

#lista inteira del :
del(minha_lista[:2])

print(minha_lista)

minha_lista2 = sorted(minha_lista2)
minha_lista2.sort(reverse=True)
print(minha_lista2)
